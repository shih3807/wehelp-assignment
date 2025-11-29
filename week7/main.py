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


@app.get("/api/member/{member_id}")
async def search_member(
    request:Request,
    member_id:int
):
    if not request.session.get("LOGGED_IN"):
        return {"data": None}

    cursor.execute("SELECT id, name, email FROM member WHERE id = %s", (member_id,))
    result = cursor.fetchone()
    if not result:
        return {"data": None}

    id = result[0]
    name = result[1]
    email = result[2]

    searcher_id = request.session.get("USER_ID")

    if member_id != searcher_id:
        cursor.execute(
            "INSERT INTO member_query(member_id, searcher_id) VALUES(%s, %s)",
            (member_id, searcher_id),
        )
        website.commit()

    return{"data":{"id":id, "name":name, "email":email}}


@app.patch("/api/member")
async def update_member_name(request: Request):

    if not request.session.get("LOGGED_IN"):
        return {"error": True}

    data = await request.json()
    new_name = data.get("name")
    user_id = request.session.get("USER_ID")

    try:
        cursor.execute("UPDATE member SET name = %s WHERE id = %s", (new_name, user_id))
        website.commit()
        request.session["USER_NAME"] = new_name
        return {"ok": True}
    except Exception as e:
        return {"error": True}


@app.get("/api/member-query")
async def get_member_query(request: Request):

    if not request.session.get("LOGGED_IN"):
        return RedirectResponse("/", status_code=303)

    member_id = request.session.get("USER_ID")
    cursor.execute(
        """
        SELECT member.name, member_query.time 
        FROM member_query
        LEFT JOIN member ON member_query.searcher_id = member.id
        WHERE member_query.member_id = %s
        ORDER BY member_query.time DESC
        LIMIT 10
        """,
        (member_id,),
    )
    results = cursor.fetchall()

    data = [
        {"name": name, "time": t.strftime("%Y-%m-%d %H:%M:%S")} for name, t in results
    ]

    return {"data": data}

