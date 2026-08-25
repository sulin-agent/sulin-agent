import requests
import json
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data= r.json()
print('返回的内容:',data)

zidian = {'用户ID':data['userId'],'标题':data['title'],"完成状态": data["completed"]}
with open('todo.json','w',encoding="utf-8") as g:
    json.dump(zidian,g,ensure_ascii=False, indent=2)

with open('todo.json','r',encoding="utf-8") as g:
    data = json.load(g)
print('读回的内容:',data)