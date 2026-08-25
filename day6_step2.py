import json

# ===== 第 1 部分：字典 → JSON 文件（存）=====
records = {
    "2026-08-20": 80.5,
    "2026-08-21": 80.2,
    "2026-08-22": 79.8,
}

with open("weight.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
print("已存成 weight.json")

# ===== 第 2 部分：JSON 文件 → 字典（读回）=====
with open("weight.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print("读回来的字典：", data)
print("8-22 的体重是：", data["2026-08-22"])
