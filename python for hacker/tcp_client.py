import socket

target_host = "127.0.0.1"
target_port = 9999

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host,target_port))


# 发送一些数据
client.send("hhhhhh".encode(encoding="utf-8"))    # 转换编码

#接收一些数据
response = client.recv(4096)

print(response)