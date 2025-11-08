from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
import json
import urllib.request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="zse4rgbnji9o;/")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse(request=request,
                                          name="index.html")


@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    if not request.session.get("LOGGED_IN"):
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse(request=request, name="menber_page.html")


@app.get("/ohoh", response_class=HTMLResponse)
async def error_page(request: Request, msg: str):
    return templates.TemplateResponse(
        request=request, name="error_page.html", context={"msg": msg}
    )

@app.post("/login")
async def login(request:Request, email: Annotated[str, Form()], password:Annotated[str,Form()]):
    if email == "abc@abc.com" and password == "abc":
        request.session["LOGGED_IN"] = True
        return RedirectResponse("/member", status_code=303)
    elif email == "" or password =="":
        msg = "請輸入信箱和密碼"
        return RedirectResponse(f"/ohoh?msg={msg}", status_code=303)
    else:
        msg = "信箱或密碼輸入錯誤"
        return RedirectResponse(f"/ohoh?msg={msg}", status_code=303)

@app.get("/logout")
async def logout(request:Request):
    request.session["LOGGED_IN"] = False
    return RedirectResponse("/", status_code=303)


def request_url(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

url_hotels_ch = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
url_hotels_en = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

html_hotels_ch = request_url(url_hotels_ch)
html_hotels_en = request_url(url_hotels_en)


data_hotels_ch = json.loads(html_hotels_ch)
data_hotels_en = json.loads(html_hotels_en)

dict_hotels_en = {}

for item in data_hotels_en["list"]:
    dict_hotels_en[int(item["_id"])] = {
        "hotel name": item["hotel name"],
    }

dict_hotels_information = {}

for item in data_hotels_ch["list"]:
    dict_hotels_information[int(item["_id"])] = {
        "name_ch": item["旅宿名稱"],
        "en_name": dict_hotels_en[int(item["_id"])]["hotel name"],
        "phone": item["電話或手機號碼"],
    }

@app.get("/hotel/{hotel_id}", response_class = HTMLResponse)
async def hotel_page(request:Request, hotel_id:int):
    hotel_information = dict_hotels_information.get(hotel_id)
    return templates.TemplateResponse(
        request=request,
        name="hotel_page.html",
        context={"hotel_information": hotel_information}
    )

