import tkinter as tk
from tkinter import*
import customtkinter as ct
from tkinter import ttk
from PIL import Image, ImageTk
from Khach import pytoex
from tkinter import messagebox
from Camera import camera
#Lấy 30 bức ảnh từ camera
def getIMG():
    c = camera.Photo(id=var_lstCus.get())
    if (c.id.startswith("KH") == False):
        messagebox.showinfo("Thông báo","Mã khách không hợp lệ")
        return  
    c.getFace()
    #Cho máy train khuôn mặt
    camera.trainFace()
#Mở camera để nhận diện
def opencamera():
    camera.recog()
#Frame chứa các component về camera
def detailCamFrame(root):
    window = Frame(root,width=650,height=400)
    global var_lstCus,lbinfo,lbSecond
    lb1 = Label(window,text="Mã khách cần lấy ảnh: ",font="Arial 20",background="#FFF1DC")
    var_lstCus = StringVar()
    ds = []
    #Đổ dữ liệu là mã khách vào ds
    for i in pytoex.getlst():
        ds.append(i[3])
    ds = tuple(ds)
    cb = ttk.Combobox(window,textvariable=var_lstCus,font="Arial 20")
    cb["values"] = ds
    
    lb1.place(x=0,y=0)
    cb.place (x = 310,y=0)
    btn1 = Button(window,text="Lấy ảnh",width=15,height=5,fg="#194485",background="#FFF1DC",font="arial 15",command=getIMG)
    btn2 = Button(window,text="Bật Camera",width=15,height=5,fg="#194485",background="#FFF1DC",font="arial 15",command=opencamera)

    btn1.place(x=100,y=100)
    btn2.place(x=350,y=100)
    
    lbinfo = Label(window,text="Hãy để mặt trước Camera để nhận diện chính xác", font="arial 15")
    lbinfo2 = Label(window,text="Nhấn ESC để thoát chế độ bật Camera", font="arial 15")
    lbinfo.place(x=100,y=350)
    lbinfo2.place(x=100,y=320)
    
    
    return window