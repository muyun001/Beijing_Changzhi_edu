import requests

res = requests.get("https://www.baidu.com")
# print(res.text)
print(res.cookies)

r = requests.get("https://www.httpbin.org/get")
r = requests.post("https://www.httpbin.org/post")
r = requests.put("https://www.httpbin.org/put")
r = requests.delete("https://www.httpbin.org/delete")
r = requests.patch("https://www.httpbin.org/patch")
print(r.text)