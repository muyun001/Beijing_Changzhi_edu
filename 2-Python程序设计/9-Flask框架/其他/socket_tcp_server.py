"""
tcp 服务端
"""
# 引入socket
import socket
# 创建socket对象 第一个参数表示ipv4   第二个参数表示使用tcp协议
sk_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
sk_server.bind(('127.0.0.1', 8080))
#sk_server.bind(('172.18.22.247', 8080))
# 需要监听客户端请求,参数为监听个数
sk_server.listen(40)
# 循环处理
while True:
    print("等待连接请求........")
    # 需要和客户端建立连接,会一直等待客户端请求
    conn, addr = sk_server.accept()
    # 取得客户端请求信息,recv需要传递大小
    data = conn.recv(1024 * 6)
    # 注意，返回的结果和发送的内容都需要是 bytes类型
    print(data)
    # 响应信息：先发送响应头部信息
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send('<html><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><h1> 我是2班学生</h1></html>'.encode('utf-8'))
    # 关闭连接
    print("已经发送响应内容........")
    conn.close()
