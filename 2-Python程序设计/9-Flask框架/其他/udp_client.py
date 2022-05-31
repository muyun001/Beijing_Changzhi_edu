# 1 引入socket模块
import socket
# 2.创建socket句柄  ，确定连接方式
sk_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('127.0.0.1', 8001)

while True:
    content = input("我>>>")
    if content == '退出':
        break
    sk_client.sendto(content.encode('utf-8'), server_addr)
    # 等待服务端回复
    data, server_addr = sk_client.recvfrom(1024*6)
    print(f"女朋友来电：{data.decode('utf-8')}")
sk_client.close()