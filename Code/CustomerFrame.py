import tkinter as tk
from tkinter import*
import customtkinter as ct
from tkcalendar import *
from tkinter import ttk
from PIL import Image, ImageTk
from Phong import Phong
from Khach import pytoex
from tkinter import messagebox
import tree
def addCus():
    for i in lstC:
        if i[3] == str(en_c1.get()):
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
    if pytoex.checkinfo(str(en_c1.get()),str(en_c2.get()),str(en_c4.get())) == False:
        messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
        return
    else:
        item = [str(en_c2.get()),str(en_c3.get_date()),str(en_c4.get()),str(en_c1.get()),str(en_c5.get()),"",str(en_c7.get_date())]          
        lstC.append(item)
        pytoex.newExcel(lstC)
        treeC.insert('',END,values=(item[3],item[0],item[4],item[2]))
def delcus():
    try:
        select = treeC.selection()[0]
        item = treeC.item(select)['values']
        t=0
        for i in range(0,len(lstC)):
            if(item[0]==lstC[i][3]):
                lstC.remove(lstC[i])
                t=1
                pytoex.newExcel(lstC)
                treeC.delete(select)
                break
        if t == 0:
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
    except IndexError:
        pass
def fixCus():
    try:
        select = treeC.selection()[0]
        item = treeC.item(select)['values']
        value=str(en_c1.get())
        if (value != item[0]):
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
        t=0
        for i in range(0,len(lstC)):
            if(item[0]==lstC[i][3]):
                lstC[i]=[str(en_c2.get()),str(en_c3.get_date()),str(en_c4.get()),str(en_c1.get()),str(en_c5.get()),"",str(en_c7.get_date())]
                t=1
                pytoex.newExcel(lstC)
                treeC.item(select,values=(lstC[i][3],lstC[i][0],lstC[i][4],lstC[i][2]))
                break
        if t == 0:
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
    except IndexError:
        pass
def showCus(event):
        try:
            select = treeC.selection()[0]
            item = treeC.item(select)['values']
            en_c1.delete(0,END)
            en_c2.delete(0,END)
            en_c4.delete(0,END)
            en_c5.delete(0,END)
            for i in lstC:
                if i[3] == item[0]:
                    en_c1.insert(0,i[3])
                    en_c2.insert(0,i[0])
                    en_c4.insert(0,i[2])
                    en_c5.insert(0,i[4])
                    en_c3.selection_set(i[1])
                    en_c7.selection_set(i[6])
        except IndexError:
            pass

def detailCusFrame(root):
    var_lstRoom = StringVar()
    ds = []
    for i in Phong.Room.toLstObj():
        ds.append(i.roomId)
    ds = tuple(ds)
    window = Frame(root,width=280,height=580,background="white")
    global en_c1,en_c2,en_c3,en_c4,en_c5,en_c7
    #Khach
    lb_c1 = Label(window,text="Mã khách: ",background="#FFF1DC")
    lb_c2 = Label(window,text ="Họ tên: ",background="#FFF1DC")
    lb_c3 = Label(window,text="Ngày sinh: ",background="#FFF1DC")
    lb_c4 = Label(window,text="SĐT(+84):",background="#FFF1DC")
    lb_c5 = Label(window,text="Phòng: ",background="#FFF1DC")
    lb_c7 = Label(window,text="Ngày thuê: ",background="#FFF1DC")
    en_c1 = Entry(window,background="#E8D5C4")
    en_c2 = Entry(window,background="#E8D5C4")
    en_c3 = Calendar(window,selectmode = 'day',year = 1995,month=1,day = 1)
    en_c4 = Entry(window,background="#E8D5C4")
    en_c5 = ttk.Combobox(window,textvariable=var_lstRoom,background="#E8D5C4")
    en_c5['values'] = ds
    en_c7 = Calendar(window,selectmode = 'day',year = 2023,month=1,day = 1)
    
    lb_c1.place(x=20,y=210)
    lb_c2.place(x=20,y=240)
    lb_c3.place(x=110,y=0)
    lb_c4.place(x=20,y=270)
    lb_c5.place(x=20,y=300)
    lb_c7.place(x=110,y=330)
    
    en_c1.place(x=120,y=210)
    en_c2.place(x=120,y=240)
    en_c3.place(x=15,y=20)
    en_c4.place(x=120,y=270)
    en_c5.place(x=120,y=300)
    en_c7.place(x=15,y=350)
    btn_c1 = Button(window,text="Thêm",command=addCus,width=10,background="#194485",fg="white")
    btn_c2 = Button(window,text="Xóa",command=delcus,width=10,background="#194485",fg="white")
    btn_c3 = Button(window,text="Sửa",command=fixCus,width=10,background="#194485",fg="white")
    btn_c1.place(x=0,y=550)
    btn_c2.place(x=100,y=550)
    btn_c3.place(x=200,y=550)
    return window
def cusTableFrame(root):
    window = Frame(root,width=650,height=280)
    global treeC,lstC
    lstC = pytoex.getlst()
    treeC = tree.getTC(window)
    treeC = tree.reload3(treeC)
    treeC.bind("<<TreeviewSelect>>", showCus)
    treeC.place(x=0,y=0)
    return window