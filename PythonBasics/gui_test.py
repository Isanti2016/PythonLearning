# -*- coding:utf-8 -*-
#此文件使用python2版本

from Tkinter import *
import tkMessageBox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='hello',command=self.hello)
        self.alertButton.pack()


        self.helloLabel=Label(self,text='hello,world!')
        self.helloLabel.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)


if __name__=='__main__':
    root=Tk()
    root.geometry('400x350+500+200')
    app=Application(root)
    app.master.title('hello,world!')
    app.mainloop()
