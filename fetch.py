import requests

r = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = r.json()

print("姓名：", data["name"])
print("邮箱：", data["email"])
print("所在城市：", data["address"]["city"])
print("经度：", data["address"]["geo"]["lng"])
