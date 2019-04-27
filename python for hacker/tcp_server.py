#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-04-27 10:04 
# @Author : Garden
# @Site :  
# @File : tcp_server.py 

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on %s:%d " % (bind_ip, bind_port))


# 这是客户处理线程
def handle_client(client_socket):
    # 打印出客户端发送的内容
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # 返回一个数据包
    client_socket.send("ACK!".encode())
    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d " % (addr[0], addr[1]))
    # 挂起客户端线程，处理传入的数据
    client_handle = threading.Thread(target=handle_client, args=(client,))
    client_handle.start()
