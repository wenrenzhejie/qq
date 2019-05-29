import tkinter
import tkinter.messagebox
def login():
    name=entryName.get()
    pwd = entryPwd.get()
    if name == 'admin' and pwd == '123456':
        tkinter.messagebox.showinfo(title='tkinter',message='Ok')
    else:
        tkinter.messagebox.showinfo(title='tkinter',message='Error')
def cancel():
    varName.set('')
    varPwd.set('')

root=tkinter.Tk()
varName=tkinter.StringVar(value='')
varPwd=tkinter.StringVar(value='')

labelName=tkinter.Label(root,text='User Name:',justify=tkinter.RIGHT,width=80)
labelName.place(x=10,y=5,width=80,height=20)

entryName=tkinter.Entry(root,width=80,textvariable=varName)
entryName.place(x=100,y=5,width=80,height=20)

labelPwd=tkinter.Label(root,text='User pwd:',justify=tkinter.RIGHT,width=80)
labelPwd.place(x=10,y=30,width=80,height=20)


entryPwd=tkinter.Entry(root,show='*',width=80,textvariable=varPwd)
entryPwd.place(x=100,y=30,width=80,height=20)

buttonOk=tkinter.Button(root,text='Ok',command=login)
buttonOk.place(x=30,y = 70,width=50,height=20)
buttonCancel=tkinter.Button(root,text='Cancel',command=cancel)
buttonCancel.place(x=90,y = 70,width=50,height=20)

root.mainloop()