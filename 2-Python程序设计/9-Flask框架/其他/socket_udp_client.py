"""
udp client客户端
"""
# 1.引入socket
import socket
# 创建cdp socket对象,注意 udp第二个参数为socket.SOCK_DGRAM
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 服务端地址
server_addr = ('127.0.0.1', 8080)

# 循环和服务器进行交互
while True:
    # 输入内容:
    my_input = input('我>>>：')
    # 注意 将内容转为bytes类型,sendto需要2个参数 a、bytes内容  b地址
    udp_client.sendto(my_input.encode('utf-8'), server_addr)
    # 接收信息
    # udp接收客户端信息recvfrom ,返回2个内容
    data, addr = udp_client.recvfrom(1024 * 6)
    print('朋友>>>：', data.decode('utf-8'))
udp_client.close()