import requests

url="https://www.gaokao.cn/school/31"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
req = requests.get(url, headers=headers)
req.encoding = req.apparent_encoding
print(req.text)