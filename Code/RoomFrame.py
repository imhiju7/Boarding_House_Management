import tkinter as tk
from tkinter import*
from tkcalendar import *
from Phong import Phong
from Phong import reloadDB
from Khach import pytoex
from tkinter import messagebox
import tree
def addRoom():
    try:
        t = 1
        for i in lstR:
            if i.roomId == str(en_r1.get()):
                t = 0
        if Phong.checkRInfo(str(en_r1.get()),str(en_r2.get()),str(en_r3.get())) == False:
            t = 0
        if t == 0:
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
        else:
            r = Phong.Room(str(en_r1.get()),str(en_r2.get()),'trong',str(en_r3.get()))
            lstR.append(r)
            reloadDB.reloadDB_ROOM(lstR)
            treeR.insert('',END,values=(r.roomId,r.square,r.status,r.maxPeople))
            return
    except IndexError:
        pass
def delRoom():
    try:
        t = 0
        select = treeR.selection()[0]
        item = treeR.item(select)['values']
        for i in range(0,len(lstR)):
            if(item[0]==lstR[i].roomId):
                if (len(lstR[i].getlstCus()) != 0):
                    messagebox.showinfo("Thông báo","Phòng có người, hãy xóa người trước!")
                    return
                else:
                    lstR.remove(lstR[i])
                    t=1
                    reloadDB.reloadDB_ROOM(lstR)
                    treeR.delete(select)
                    break
        if t == 0:
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
    except IndexError:
        pass
def fixRoom():
    t = 0
    select = treeR.selection()[0]
    item = treeR.item(select)['values']
    if Phong.checkRInfo(str(en_r1.get()),str(en_r2.get()),str(en_r3.get())) == False:
        t = 0
    for i in range(0,len(lstR)):
        if(item[0]==lstR[i].roomId):
            t=1
            lstR[i].square = float(en_r2.get())
            lstR[i].maxPeople = int(en_r3.get())
            reloadDB.reloadDB_ROOM(lstR)
            treeR.item(select,values=(str(en_r1.get()),str(en_r2.get()),lstR[i].status,str(en_r3.get())))
            break
    if t == 0:
        messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
def showRoom(event):
    try:
        select = treeR.selection()[0]
        item = treeR.item(select)['values']
        en_r1.delete(0,END)
        en_r2.delete(0,END)
        en_r3.delete(0,END)
        for i in lstR:
            if i.roomId == item[0]:
                tx1.config(state=NORMAL)
                tx1.delete("1.0","end")
                s = ""
                for j in lstC:
                    if j[4] == item[0]:
                        s += j[0] + "\n"
                en_r1.insert(0,i.roomId)
                en_r2.insert(0,i.square)
                en_r3.insert(0,i.maxPeople)
                if (s == ""):
                    tx1.insert(END,"Phòng này chưa có người ở!")
                else:
                    tx1.insert(END,s)
                tx1.config(state=DISABLED)
                break
    except IndexError:
        pass
def detailRoomFrame(root):
    window = Frame(root,width=280,height=580,background="white")
    
    global tx1,lb_r1,lb_r2,lb_r3,en_r1,en_r2,en_r3
    tx1= Text(window,width=30,height=10,state=DISABLED)
    lb_r1 = Label(window,text="Phòng: ",background="#FFF1DC")
    lb_r2 = Label(window,text="Diện tích(m2): ",background="#FFF1DC")
    lb_r3 = Label(window,text="Số người tối đa: ",background="#FFF1DC")
    en_r1 = Entry(window,background="#E8D5C4")
    en_r2 = Entry(window,background="#E8D5C4")
    en_r3 = Entry(window,background="#E8D5C4")
    btn_r1= Button(window,width=10,text="Thêm",background="#194485",fg="white")
    btn_r2= Button(window,width=10,text="Xóa",background="#194485",fg="white")
    btn_r3= Button(window,width=10,text="Sửa",background="#194485",fg="white")
    
    tx1.place(x=0,y=0)
    lb_r1.place(x=20,y=210)
    lb_r2.place(x=20,y=240)
    lb_r3.place(x=20,y=270)
    en_r1.place(x=120,y=210)
    en_r2.place(x=120,y=240)
    en_r3.place(x=120,y=270)
    btn_r1 = Button(window,text="Thêm",command=addRoom,width=10,background="#194485",fg="white")
    btn_r2 = Button(window,text="Xóa",command=delRoom,width=10,background="#194485",fg="white")
    btn_r3 = Button(window,text="Sửa",command=fixRoom,width=10,background="#194485",fg="white")
    btn_r1.place(x=0,y=550)
    btn_r2.place(x=100,y=550)
    btn_r3.place(x=200,y=550)
    return window
def tableRoomFrame(root):
    window = Frame(root,width=650,height=280)
    global lstR,treeR,lstC
    lstC = pytoex.getlst()
    lstR = Phong.Room.toLstObj()
    reloadDB.reloadDB_ROOM(lstR)
    lstR = Phong.Room.toLstObj()
    treeR = tree.getRT(window)
    treeR = tree.reload4(treeR)
    treeR.bind("<<TreeviewSelect>>", showRoom)
    treeR.place(x=0,y=0)
    return window