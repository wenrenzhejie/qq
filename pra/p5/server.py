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
    print("一个客户端连接进来",conn,addr,type(addr[0]),type(addr[1]))
    username = conn.recv(1024)
    username = username.decode()
    print(username,type(username))
    #如果没设置用户名，则将其用户名设置为ip：port
    if username == 'no':
        username= addr[0]+":"+str(addr[10])

    print(username)
    users.append((conn,username,addr))
    try:
        while True:
            recdata = conn.recv(1024)
            recdata = recdata.decode()
            print(type(recdata))
            deposit(addr, recdata)
    except Exception as e:
        deleteUsers(conn)
        conn.close()

def sendMessage():
    while True:
        if not que.empty():
                data = que.get()
                print(data,type(data[1]))
                for c0 in users:
                    for c1 in users:
                        if c1[2] == data[0]:
                            print("进来了")
                            msg = c1[1]+":"+data[1]
                            break
                    c0[0].send(msg.encode())
def deposit(addr, data):
    try:
        lock.acquire()
        que.put((addr, data))
    finally:
        lock.release()

def deleteUsers(conn):
    a = 0
    for i in users:
        if i[0] == conn:
            users.pop(a)
            print("剩余在线用户:", users)
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
