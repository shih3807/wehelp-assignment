import urllib.request
import time, random
import csv
from bs4 import BeautifulSoup

BASE_URL = "https://www.ptt.cc"

def fetch_url(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
    }
    request = urllib.request.Request(url, headers=header)
    with urllib.request.urlopen(request) as respon:
        html = respon.read().decode("utf-8")
        time.sleep(1 + random.random())
        return html

def serch_in_page(page_html):
    soup = BeautifulSoup(page_html, "html.parser")
    articles = []

    for div_article in soup.find_all("div", class_ = "r-ent"):
        if div_article.find_previous_sibling("div", class_="r-list-sep"):
            break
        div_title = div_article.find("div", class_ = "title")
        if div_title and div_title.a:
            title = div_title.a.text
            article_link = BASE_URL + div_title.a["href"]
        else:
            title = "文章已刪除"
            article_link = None

        div_like = div_article.find("div", class_ = "nrec")
        if div_like and div_like.span:
            like = div_like.span.text
        else:
            like = 0

        articles.append({"title":title, "like":like, "article_link":article_link})

    return articles


def search_in_articles(article_html):
    soup = BeautifulSoup(article_html, "html.parser")
    span = soup.find_all("span", class_="article-meta-value")
    span_2 = soup.find_all("span", class_="b4")
    if len(span) >= 3:
        date = span[3].text
    elif len(span_2)>= 3:
        date = span_2[3].text
    else:
        date = None
    return date


page_url = BASE_URL + "/bbs/Steam/index.html"
all_articles=[]

for i in range(3):
    html = fetch_url(page_url)
    articles = serch_in_page(html)

    for art in articles:
        if art["article_link"]:
            art_html = fetch_url(art["article_link"])
            date = search_in_articles(art_html)
            title = art["title"]
            like = art["like"]
            all_articles.append({"title":title, "like":like, "date":date})

    soup = BeautifulSoup(html, "html.parser")
    btn =  soup.find_all("a", class_="btn wide")
    prev_link = BASE_URL + btn[1]["href"]
    page_url = prev_link

with open("articles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for art in all_articles:
        writer.writerow([art["title"], art["like"], art["date"]])       
