# 抓百度翻译案例
import requests
import json

WORD = "天气"


def main():
    # post_url = "https://fanyi.baidu.com/sug"
    post_url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "Cookie": 'BAIDUID=26C2E7B3FABC4F2B2E0A8B0F73C3AF23:FG=1; BDUSS=F5T0JrUGZIcHdQWHNDZUxFd05ZSU5VV09YdWlINEl5Z2ZNc1p0Z29YU3BKSHBpRVFBQUFBJCQAAAAAAAAAAAEAAADSmXM5xsbP~jQxMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKmXUmKpl1JiMk; BDUSS_BFESS=F5T0JrUGZIcHdQWHNDZUxFd05ZSU5VV09YdWlINEl5Z2ZNc1p0Z29YU3BKSHBpRVFBQUFBJCQAAAAAAAAAAAEAAADSmXM5xsbP~jQxMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKmXUmKpl1JiMk; MCITY=-%3A; BAIDUID_BFESS=26C2E7B3FABC4F2B2E0A8B0F73C3AF23:FG=1; ZD_ENTRY=bing; BIDUPSID=26C2E7B3FABC4F2B2E0A8B0F73C3AF23; PSTM=1650544922; H_PS_PSSID=35837_31660_34813_36166_34584_36120_36341_36075_36125_35802_36234_26350_22157_36061; RT="z=1&dm=baidu.com&si=alf71djw5e&ss=l2sde15p&sl=3&tt=6it&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=b98&ul=114a&hd=11ez"; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaoldFixedStatus=false; ariaStatus=false; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651920661; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1651920661; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_NDVhYThmODRjMWE4YmVhODg3N2RkZTk3NDQ0OTE4ZmFmNGUyOGEwNTFmZDA5ODY4ZmYyNTZmZTIwMWUwYmFhZjczNTQzMTIyOGE4YjBkOGI2ZjhlZmRlMmMxNTcwZjJjZTMyMDg3OWFlNzBmNzNkOWIzZmY4YmJiZjExY2FmYTQ0ZmYzYjEwYzhlZjhhNmI0NWRmNmI2Y2IwOGQ2YmEwZGY2MGZiYWZkYTJjNDVhNDJlZmQ1ODU0ZWE0NzI1ZTdh',
    }
    # post_url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    data = {
        'from': 'en',
        'to': 'zh',
        'query': WORD,
        # 'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '54706.276099',
        'token': 'dc8cd4cae430c798860d5e27abd65966',
        'domain': 'common',
    }

    # response = requests.post(url=post_url, data=data)
    # print(response.request.headers)  # 被反爬，所以需要ua伪装

    response = requests.post(url=post_url, data=data, headers=header)
    json_data = json.loads(response.text)
    print(json_data)


if __name__ == "__main__":
    main()
