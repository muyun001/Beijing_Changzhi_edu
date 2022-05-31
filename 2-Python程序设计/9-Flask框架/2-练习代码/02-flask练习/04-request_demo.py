import requests

# get方法
url_get = "http://127.0.0.1:5000/login?name=zhangsan"
res = requests.get(url_get)
print(res.text)


# post
data = {
    "name": "lisi"
}

url_post = "http://127.0.0.1:5000/login"
res = requests.post(url_post, data=data)

print(res.text)
