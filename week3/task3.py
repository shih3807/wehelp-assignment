import urllib.request
import json

with urllib.request.urlopen("https://cwpeng.github.io/test/assignment-3-1") as f:
    data_info = json.load(f)

with urllib.request.urlopen("https://cwpeng.github.io/test/assignment-3-2") as f:
    data_pics = json.load(f)

host = data_pics["host"]

attractions = []

pics_dict = {}

for row in  data_pics["rows"]:
    first_pic = row["pics"].split(".jpg")[0]
    img_url = host + first_pic + ".jpg"
    pics_dict[row["serial"]] = img_url

for row in data_info["rows"]:
    title = row["sname"]
    serial = row["serial"]
    img_url = pics_dict.get(serial, "")
    attractions.append({"title":title, "img":img_url})

with open("attraction.json", "w", encoding="utf-8") as f:
    json.dump(attractions, f, ensure_ascii=False, indent=2)
