# https://cuiqingcai.com/3335.html

# import multiprocessing
# import time
#
#
# def process(num):
#     time.sleep(num)
#     print('Process:', num)
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#
#     # 获取电脑cpu的数量
#     print('CPU number:' + str(multiprocessing.cpu_count()))
#     # 对所有运行的进程遍历
#     for p in multiprocessing.active_children():
#         # 输出进程的名称及id
#         print('Child process name: ' + p.name + ' id: ' + str(p.pid))
#
#     print('Process Ended')


from multiprocessing import Pool
import requests
from requests.exceptions import ConnectionError


def scrape(url):
    try:
        print(requests.get(url))
    except ConnectionError:
        print('Error Occured ', url)
    finally:
        print('URL ', url, ' Scraped')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    pool.map(scrape, urls)