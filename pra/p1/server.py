import socket
from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = ''
port=10086
s.bind((ip, port))
s.listen()
print("服务器开始监听")

def tcp_connect(conn, addr):
    print(conn, addr)
    while True:
        data = conn.recv(1024)
        data = data.decode()
        print(data)


while True:
    conn, addr = s.accept()
    t = Thread(target=tcp_connect,args=(conn, addr))
    t.start()


