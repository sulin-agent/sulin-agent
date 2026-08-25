import json
chengji = {"小明": 88, "小红": 92, "小刚": 75}
with open ('scores.json','w',encoding="utf-8") as f:
    json.dump(chengji,f,ensure_ascii=False, indent=2)
print('存成scores.json')

with open ('scores.json','r',encoding='utf-8') as f:
    data = json.load(f)
print(f'小红的成绩是:{data["小红"]}')
print(f'三个人的平均分是:{(sum(data.values())/ len(chengji))}')
