import socket
import threading
from tkinter import *
import json
ip=''
port=''
user=''
# 登录窗口的图形用户界面
loginRoot=Tk()
loginRoot.title("登录")
loginRoot['height'] = 110
loginRoot['width'] = 250

ip1=StringVar()
ip1.set('127.0.0.1:10086')

user1 = StringVar()
user1.set('')

# 服务器标签
labelIP = Label(loginRoot, text='服务器地址')
labelIP.place(x=20, y=10, width=80, height=20)

entryIP = Entry(loginRoot, width=80, textvariable=ip1)
entryIP.place(x=110, y=10, width=110, height=20)

# 用户名标签
labelUser = Label(loginRoot, text='用户名')
labelUser.place(x=20, y=40, width=80, height=20)

entryUser = Entry(loginRoot, width=80, textvariable=user1)
entryUser.place(x=110, y=40, width=110, height=20)

# 登录按钮
def login(event=0):
    global ip, port, user
    ip, port = entryIP.get().split(':')  # 获取IP和端口号
    port = int(port)  # 端口号需要为int类型
    user = entryUser.get()
    loginRoot.destroy()  # 关闭窗口
loginRoot.bind('<Return>', login)

but = Button(loginRoot, text='登录', command=login)
but.place(x=90, y=70, width=70, height=30)
print("mainloopqian")
loginRoot.mainloop()
print("mainloophou")
try:
    print("scoket钱")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print("scokethou")
    if user:
        s.send(user.encode())
    else:
        s.send('no'.encode())  # 没有输入用户名则标记
except Exception as e:
    print("exe")
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

#聊天窗口的图形用户界面面
chatRoot1=Tk()
chatRoot1.title("chat")
chatRoot1.title('text')
chatRoot1['height'] = 330
chatRoot1['width'] = 450

# 创建多行文本框
listbox = Listbox(chatRoot1, width=300)
listbox.place(x=5, y=0, width=440, height=280)

# 创建输入文本框和关联变量
a = StringVar()
a.set('')
entry = Entry(chatRoot1, width=120, textvariable=a)
entry.place(x=5, y=285, width=300, height=30)

button = Button(chatRoot1, text='发送', command=sendMessage)
button.place(x=310, y=285, width=60, height=30)
chatRoot1.bind('<Return>', sendMessage)  # 绑定回车发送信息

#用于时刻从服务器端获取数据并显示
t1 = threading.Thread(target=getMessage)
t1.start()
chatRoot1.mainloop()