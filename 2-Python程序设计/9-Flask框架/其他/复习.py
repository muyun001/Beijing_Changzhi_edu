"""
复习：
网络编程: tcp编程 和udp编程
区别: tcp需要建立连接  udp无连接的
      udp不可靠，不安全
socket模块   tcp客户端、服务端  udp的客户端和服务端编程





get和post
区别：
    get有长度限制  post没有长度限制
    get在浏览器回退时时无害的 。post会重新发送请求
    get提交的地址可以被收藏 post不可以
    get不安全 因为参数暴露在浏览器地址上
    get浏览记录会被保存 post不会
    get一般使用于获取数据，查询等
    post一般用户form表单提交 ,文件上传。 get无法进行文件上传



# tcp 服务器端
# 1 引入socket模块
import socket
# 2.创建socket句柄  ，确定连接方式
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 确定绑定地址
sk.bind(('127.0.0.1', 8001))

# 对于服务器端需要进行监听
sk.listen(6)
# 循环处理响应
while True:
    # 对于tcp服务端，是被动接收请求。
    conn, addr = sk.accept()
    # 获取内容 tcp使用recv , 获取内容的类型为bytes
    data = conn.recv(1024*6)
    print(data.decode('utf-8'))
    # 进行响应处理,响应头部信息
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # 响应体
    conn.send(b'<h1>hello</h1>')
    # 关闭连接
    conn.close()
"""
"""
# UDP 服务器端
# 1 引入socket模块
import socket
# 2.创建socket句柄  ，确定连接方式
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sk.bind(('127.0.0.1', 8001))
while True:
    # 被动接受
    data, addr = sk.recvfrom(1024*6)
    # 打印内容
    print(f"{addr[1]}来电：{data.decode('utf-8')}")
    res = input("回电>>")
    if res == '退出':
        sk.sendto('我已下线'.encode('utf-8'), addr)
        break
    sk.sendto(res.encode('utf-8'), addr)
sk.close()

"""
"""
# udp 客户端时
# 1 引入socket模块
import socket #
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
"""


