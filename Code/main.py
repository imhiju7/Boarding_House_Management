from tkinter import *
import customtkinter as ct
from CustomerFrame import *
from tkcalendar import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from BillFrame import *
from RoomFrame import *
from CameraFrame import *
from InfoFrame import *
import os
cur_dir = os.path.abspath(".")
window = Tk()
f = "arial 20 bold"
#---------Switch between page
def toCustomer():
    cusFrame.place(x=825,y=100)
    tableCus.place(x=150,y=400)
    roomFrame.place_forget()
    tableRoom.place_forget()
    billFrame.place_forget()
    tableBill.place_forget()
    camFrame.place_forget()
    
def toRoom():
    cusFrame.place_forget()
    tableCus.place_forget()
    billFrame.place_forget()
    tableBill.place_forget()
    camFrame.place_forget()
    roomFrame.place(x=825,y=100)
    tableRoom.place(x=150,y=400)
def toBill():
    roomFrame.place_forget()
    tableRoom.place_forget()
    cusFrame.place_forget()
    tableCus.place_forget()
    camFrame.place_forget()
    billFrame.place(x=825,y=100)
    tableBill.place(x=150,y=400)
def toCam():
    roomFrame.place_forget()
    tableRoom.place_forget()
    cusFrame.place_forget()
    tableCus.place_forget() 
    billFrame.place_forget()
    tableBill.place_forget()
    camFrame.place(x=140,y=290)
def toInfo():
    for widget in lst_thongke:
        widget.place_forget()
    information.place(x=210,y=150)
    btn_Info.config(background="#E8D5C4")
    btn_Thongke.config(background="#053679")
def toThongKe():
    toCustomer()
    bt.place(x=136,y=120)
    bt1.place(x=310,y=120)
    bt2.place(x=478,y=120)
    bt3.place(x=650,y=120)
    lb_danhsach.place(x=136,y=290)
    lb_detail.place(x=825,y=130)
    information.place_forget()
    btn_Info.config(background="#053679")
    btn_Thongke.config(background="#E8D5C4")

#Main frame
window.title("Quản Lý Nhà Trọ")
window.geometry("1125x700+200+50")
Label(window,text="Quản Lí Nhà Trọ ",font = "arial 30 bold",fg="#194485",width=42,height=3).place(y=10,x = 110)
Label(window,text="",font = f,width=7,height=5,bg="#053679").place(y=-1)
Label(window,text="",font = f,width=7,height=20,bg="#053679").place(y=175)
Label(window,fg="#194485",font = f,height=7,width=22).place(x=126,y=103)
Label(window,fg="#194485",font = f,height=15,width=39).place(x=126,y=375)
icon_Cam=Image.open(cur_dir + "/img/other/camera.png")
img_cam=icon_Cam.resize((30,30))
my_img_cam=ImageTk.PhotoImage(img_cam)
icon_user=Image.open(cur_dir + "/img/other/user.png")
img_user=icon_user.resize((30,30))
my_img_user=ImageTk.PhotoImage(img_user)
icon_room=Image.open(cur_dir + "/img/other/room.png")
img_room=icon_room.resize((30,30))
my_img_room=ImageTk.PhotoImage(img_room)
icon_bill=Image.open(cur_dir + "/img/other/bill.png")
img_bill=icon_bill.resize((30,30))
my_img_bill=ImageTk.PhotoImage(img_bill)
icon_logout=Image.open(cur_dir + "/img/other/log_out.png")
img_logout=icon_logout.resize((30,30))

app_icon = Image.open(cur_dir + "/img/other/icon.jpg")
app_icon = app_icon.resize((120,160))
app_icon = ImageTk.PhotoImage(app_icon)

lb_icon = Label(window,image=app_icon)
app_icon.image = app_icon
lb_icon.place(x=0,y=0)
bt=ct.CTkButton(window,text="KHÁCH THUÊ ",width=65,height=90,corner_radius=10,text_color="white",fg_color="#6763FE",command=toCustomer,image=my_img_user)
bt1=ct.CTkButton(window,text="PHÒNG",width=140,height=90,corner_radius=10,text_color="white",fg_color="#00A0B6",command=toRoom,image=my_img_room)
bt2=ct.CTkButton(window,text="HÓA ĐƠN",width=140,height=90,corner_radius=10,text_color="white",fg_color="#E06B9F",command=toBill,image=my_img_bill)
bt3=ct.CTkButton(window,text="CAMERA",width=140,height=90,corner_radius=10,text_color="white",fg_color="#266FD5",command=toCam,image=my_img_cam)

lb_detail =LabelFrame(window,width=280,height=530,background="white")
lb_danhsach = Label(window,text="Danh sách  ",fg="#194485",font = f)

#Thong ke
btn_Thongke = Button(window,command=toThongKe,text="Thống kê",font="arial 15 bold",width=9,background="#053679",foreground="white")
btn_Thongke.place(y=180,x=4)

#Thong tin ca nhan
btn_Info = Button(window,command=toInfo,text="Thông tin",font='arial 15 bold',width=9,background="#053679",foreground="white")
btn_Info.place(y=225,x=4)

#Các frame để chèn vào frame main
cusFrame = detailCusFrame(window)
tableCus = cusTableFrame(window)

roomFrame = detailRoomFrame(window)
tableRoom = tableRoomFrame(window)

billFrame = detailBillFrame(window)
tableBill = tableBillFrame(window)

camFrame = detailCamFrame(window)

lst_thongke = [bt,bt1,bt2,bt3,lb_danhsach,lb_detail,cusFrame,tableCus,roomFrame,tableRoom,billFrame,tableBill,camFrame]
information = infoFrame(window)
toThongKe()

window.mainloop()
