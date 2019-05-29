import socket
import threading
import queue
import json
ip=''
port=10086
users=[]#存放所有用户
que=queue.Queue()#存放消息
lock=threading.Lock()#防止多线程并发放置消息错误

def receiveMessage(conn,addr):
    print("一个客户端连接进来",conn,addr)
    users.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            data = data.decode()
            deposit(addr, data)
    except Exception as e:
        deleteUsers(conn)
        conn.close()

def sendMessage():
    while True:
        if not que.empty():
                data = que.get()
                from1 = data[0]
                data = list(data)
                data = json.dumps(data)
                print(type(data))
                for c in users:
                    if from1 != c:
                        c.send(data.encode())

def deposit(addr, data):
    try:
        lock.acquire()
        que.put((addr, data))
    finally:
        lock.release()

def deleteUsers(conn):
    a = 0
    for i in users:
        if i == conn:
            users.pop(a)
            print("剩余在线用户:",users)
            return
        a += 1

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen()
    send = threading.Thread(target=sendMessage)
    send.start()

    while True:
        conn, addr = s.accept()
        r = threading.Thread(target=receiveMessage, args=(conn, addr))
        r.start()

main()
