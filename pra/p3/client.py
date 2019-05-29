import socket
import threading
from tkinter import *
import json
ip='127.0.0.1'
port=10086
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
except Exception as e:
    s.close()
def getMessage():
    while True:
        data = s.recv(1024)
        print(type(data),data)
        data = json.loads(data)
        print(type(data), data)
        listbox.insert(END,data)

def sendMessage():
        message=entry.get()
        print("entry:",type(message),message)
        s.send(message.encode())
        a.set('')


# 创建图形界面
root=Tk()
root.title("qq")
root.title('text')
root['height'] = 330
root['width'] = 450

# 创建多行文本框
listbox = Listbox(root, width=300)
listbox.place(x=5, y=0, width=440, height=280)

# 创建输入文本框和关联变量
a = StringVar()
a.set('')
entry = Entry(root, width=120, textvariable=a)
entry.place(x=5, y=285, width=300, height=30)

button = Button(root, text='发送', command=sendMessage)
button.place(x=310, y=285, width=60, height=30)
root.bind('<Return>', sendMessage)  # 绑定回车发送信息

#用于时刻从服务器端获取数据并显示
t1 = threading.Thread(target=getMessage)
t1.start()
root.mainloop()