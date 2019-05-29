import socket
import threading
ip='127.0.0.1'
port=10086

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

def getMessage():
    while True:
        data = s.recv(1024)
        data=data.decode()
        print(data)

def sendMessage():
    while(True):
        message=input(("请输入信息:"))
        s.send(message.encode())
        if(message == 'bye'):
            break
    s.close()


r = threading.Thread(target=getMessage)
r.start()

send = threading.Thread(target=sendMessage)
send.start()
