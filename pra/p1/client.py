import socket
from threading import Thread
ip='127.0.0.1'
port=10086
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

while True:
    message=input("请输入信息")
    s.send(message.encode())