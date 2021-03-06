# 导入socket库:
import socket
import pprint
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 8080))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost:localhost\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#pprint.pprint(data)
header, html = data.split(b'\r\n\r\n', 1)
pprint.pprint(header.decode('utf-8'))
pprint.pprint(html.decode('utf-8'))
# 把接收的数据写入文件:
with open('my.html', 'wb') as f:
    f.write(html)