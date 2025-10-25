# task1
print("=== Task 1 ===")


def func1(name):
    # 每個角色的位置
    characters = {
        "貝吉塔": {"x": -4, "y": -1, "side": 1},
        "辛巴": {"x": -3, "y": 3, "side": 1},
        "丁滿": {"x": -1, "y": 4, "side": 0},
        "悟空": {"x": 0, "y": 0, "side": 1},
        "特南克斯": {"x": 1, "y": -2, "side": 1},
        "弗利沙": {"x": 4, "y": -1, "side": 0},
    }
    # 角色間的距離
    position = characters[name]
    arr1 = []
    # 放名字和距離
    arr2 = []
    # 比大小
    for character_name in characters:
        distance = abs(position["x"] - characters[character_name]["x"]) + abs(
            position["y"] - characters[character_name]["y"]
        )
        if distance == 0:
            continue
        if position["side"] == characters[character_name]["side"]:
            arr1.append({"name": character_name, "distance": distance})
            arr2.append(distance)
        else:
            arr1.append({"name": character_name, "distance": distance + 2})
            arr2.append(distance + 2)

    # 得出最遠與最近
    farthest = []
    nearest = []
    for i in range(len(arr1)):
        if arr1[i]["distance"] == max(arr2):
            farthest.append(arr1[i]["name"])
    for i in range(len(arr1)):
        if arr1[i]["distance"] == min(arr2):
            nearest.append(arr1[i]["name"])

    print("最遠" + "、".join(farthest) + "；最近" + "、".join(nearest))


func1("辛巴")
func1("悟空")
func1("弗利沙")
func1("特南克斯")


# task2
import re

print("=== Task 2 ===")
# 服務
services = [
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800},
]
# 時間
schedule = []
for i in range(24):
    schedule.append({"t": i, "S1": True, "S2": True, "S3": True})
# 標準
standard = ["r", "c"]


def func2(ss, start, end, criteria):
    # 拆字串
    def separation(string):
        match = re.match(r"^([a-z]+)([<>=]+)([\dA-Za-z.]+)$", string)
        standard = match.group(1)
        operator = match.group(2)
        value = match.group(3)
        return {"standard": standard, "operator": operator, "value": value}

    requirement = separation(criteria)
    # requirement["standard"]：前面的單位
    # requirement["operator"]：中間比較符號
    # requirement["value"]：最後數字或名字

    # 預約時間
    def reservation(service_name):
        if schedule[start][service_name] and schedule[end - 1][service_name]:
            for i in range(start, end):
                schedule[i][service_name] = False
            print(service_name)
        else:
            print("sorry")

    if requirement["standard"] == "name":
        reservation(requirement["value"])
    else:
        n = float(requirement["value"])

        if requirement["operator"] == "<=":
            if requirement["standard"] in standard:
                Max = sorted(
                    [item for item in services if item[requirement["standard"]] <= n],
                    key=lambda x: x[requirement["standard"]],
                    reverse=True,
                )
                found = False
                for service in Max:
                    if (
                        schedule[start][service["name"]]
                        and schedule[end - 1][service["name"]]
                    ):
                        reservation(service["name"])
                        found = True
                        break
                if not found:
                    print("Sorry")
        elif requirement["operator"] == ">=":
            if requirement["standard"] in standard:
                Min = sorted(
                    [item for item in services if item[requirement["standard"]] >= n],
                    key=lambda x: x[requirement["standard"]],
                )
                found = False
                for service in Min:
                    if (
                        schedule[start][service["name"]]
                        and schedule[end - 1][service["name"]]
                    ):
                        reservation(service["name"])
                        found = True
                        break
                if not found:
                    print("Sorry")


func2(services, 15, 17, "c>=800")
func2(services, 11, 13, "r<=4")
func2(services, 10, 12, "name=S3")
func2(services, 15, 18, "r>=4.5")
func2(services, 16, 18, "r>=4")
func2(services, 13, 17, "name=S1")
func2(services, 8, 9, "c<=1500")


# task3
import math

print("=== Task 3 ===")


def func3(index):
    x = index // 4
    y = index % 4
    z = 25 + x * -2
    if y == 1:
        print(z - 2)
    elif y == 2:
        print(z - 5)
    elif y == 3:
        print(z - 4)
    else:
        print(z)


func3(1)
func3(5)
func3(10)
func3(30)


# task4
print("=== Task 4 ===")


def func4(sp, stat, n):
    available = list(stat)
    carriages = []
    for i in range(len(sp)):
        seat = sp[i]
        able = available[i]
        carriages.append(
            {"carriage_number": i, "seat": seat, "able": able, "closest": abs(seat - n)}
        )

    nearest = []
    for i in range(len(sp)):
        if carriages[i]["able"] == "1":
            continue
        nearest.append(carriages[i]["closest"])

    best = []
    for i in range(len(sp)):
        if carriages[i]["able"] == "1":
            continue
        elif carriages[i]["closest"] == min(nearest):
            best.append(carriages[i]["carriage_number"])

    print("、".join(map(str, best)))


func4([3, 1, 5, 4, 3, 2], "101000", 2)
func4([1, 0, 5, 1, 3], "10100", 4)
func4([4, 6, 5, 8], "1000", 4)
