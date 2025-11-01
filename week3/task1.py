# Task1
import urllib.request
import json
import csv
from collections import Counter
from collections import defaultdict
import re

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
for list in data_hotels_en["list"]:
    dict_hotels_en[int(list["_id"])]= {
        "hotel name": list["hotel name"],
        "address": list["address"],
    }


with open("hotels.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for list in data_hotels_ch["list"]:
        writer.writerow(
            [
                list["旅宿名稱"],
                dict_hotels_en[int(list["_id"])]["hotel name"],
                list["地址"],
                dict_hotels_en[int(list["_id"])]["address"],
                list["電話或手機號碼"],
                list["房間數"],
            ]
        )

# areas = []
# for d in data_hotels_ch["list"]:
#     find_area = re.search(r"臺北市(.+?[區])", d["地址"])
#     if find_area:
#         areas.append([find_area.group(1)])

#     else:
#         areas.append("沒有區域")

# area_count = Counter(areas)

# with open("districts_1.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     for area,count in area_count.items():
#         writer.writerow([area, count])

# area_stats = defaultdict(lambda:{"hotel_count":0, "room_count":0})

# for d in data_hotels_ch["list"]:
#     find_area = re.search(r"臺北市(.+?區)", d["地址"])
#     if find_area:
#         area = find_area.group(1)
#         area_stats[area]["hotel_count"] += 1
#         area_stats[area]["room_count"] += int(d["房間數"])
#     else:
#         area = "沒有區域"
#         area_stats[area]["hotel_count"] += 1
#         area_stats[area]["room_count"] += int(d["房間數"])


# with open("districts.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     for area, stats in area_stats.items():
#         writer.writerow([area, stats["hotel_count"],stats["room_count"] ])
