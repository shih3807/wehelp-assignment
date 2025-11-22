from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
import config

app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name="static")
template = Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware, secret_key=config.SESSION_MIDDLEWARE_SECRET_KEY)

website = mysql.connector.connect(
    host="localhost", 
    user=config.DB_USER, 
    password=config.DB_PASSWORD,
    database = "website"
)

cursor = website.cursor()

@app.get("/", response_class = HTMLResponse)
async def read_root(request:Request):
    return template.TemplateResponse(request = request, name = 'index.html')


@app.get("/ohoh", response_class=HTMLResponse)
async def error_page(request: Request, msg: str):
    return template.TemplateResponse(
        request=request, name="error_page.html", context={"msg": msg}
    )


@app.post("/signup")
async def signup(request:Request, name:Annotated[str, Form()], email:Annotated[str, Form()], password:Annotated[str, Form()]):
    cursor.execute("SELECT id FROM member WHERE email = %s", (email.lower(),))
    result = cursor.fetchone()

    if result:
        return {"status":"error", "msg": "重複的電子郵件"}

    cursor.execute(
        "INSERT INTO member(name, email, password) VALUES(%s, %s, %s)",
        (name, email, password),
    )
    website.commit()

    return{"status":"ok", "msg": "成功註冊！"}

@app.post("/login")
async def signup(
    request: Request,
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    cursor.execute(
        "SELECT id, name, email, password FROM member WHERE email = %s ", (email.lower(),)
    )
    result = cursor.fetchone()

    if not result:
        return {"status": "error", "msg": "電子郵件或密碼錯誤"}
    member_id = result[0]
    member_name = result[1]
    member_email = result[2]
    member_password = result[3]

    if  member_password != password:
        return {"status": "error", "msg": "電子郵件或密碼錯誤"}

    request.session["LOGGED_IN"] = True
    request.session["USER_ID"] = member_id 
    request.session["USER_NAME"] = member_name
    request.session["USER_EMAIL"] = member_email
    return {"status": "ok"}


@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if not request.session.get("LOGGED_IN"):
        return RedirectResponse("/", status_code=303)

    cursor.execute(
        "SELECT message.id, member.name, message.content  \
        FROM message \
        LEFT JOIN member \
        ON message.member_id = member.id \
        ORDER BY message.time DESC;"
    )
    messages = cursor.fetchall()

    user_name = request.session.get("USER_NAME")
    return template.TemplateResponse(
        request=request,
        name="member.html",
        context={"user_name": user_name, "messages": messages},
    )


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


@app.post("/createMessage")
async def create_message(
    request: Request,
    message: Annotated[str, Form()],
):
    id = request.session.get("USER_ID")
    cursor.execute(
        "INSERT INTO message(member_id, content) VALUES(%s, %s)",
        (id, message)
    )
    website.commit()

    return RedirectResponse("/member", status_code=303)


@app.post("/deleteMessage")
async def delete_message(
    request: Request,
    message_id: Annotated[int, Form()],
):

    cursor.execute("DELETE FROM message WHERE id = %s", (message_id,))
    website.commit()

    return RedirectResponse("/member", status_code=303)
