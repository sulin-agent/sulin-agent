import requests

# 发一个 GET 请求（相当于浏览器打开这个网址）
r = requests.get("https://httpbin.org/get")

print("状态码：", r.status_code)        # 200 表示成功
print("返回的内容类型：", r.headers.get("Content-Type"))

# 把返回的 JSON 字符串，解析成 Python 字典
data = r.json()
print("我电脑的公网 IP:", data["origin"])
print("我请求的网址：", data["url"])
