"""
udp server
"""
# 1.引入socket
import socket
# 创建cdp socket对象,注意 udp第二个参数为socket.SOCK_DGRAM
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址 ,1个参数为元组
#udp_server.bind(('127.0.0.1', 8080))
udp_server.bind(('172.18.22.247', 8080))
# 循环接收信息
print("好痛苦，没人和我聊天")
while True:
    # udp接收客户端信息recvfrom ,返回2个内容
    data, addr = udp_server.recvfrom(1024 * 6)
    # 注意返回和提交的数据为bytes类型
    print(f"{addr}-->", data.decode('utf-8'))
    # 服务器响应，输入内容
    send_content = input(f'回复:{addr}>>')
    # 发送信息 udp为sendto ,需要2个参数，a、内容 b、接收地址
    udp_server.sendto(send_content.encode('utf-8'), addr)

udp_server.close()