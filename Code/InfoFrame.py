from tkinter import *
from PIL import Image, ImageTk
import os
cur_dir = os.path.abspath(".")

def infoFrame(root):
    window = Frame(root,width=825,height=500)
    bg = Image.open(cur_dir + "/img/other/bg.jpg")
    bg = bg.resize((840,280))
    bg = ImageTk.PhotoImage(bg)
    lb_info_content = Label(window,text="",width=120,height=12,background="white")
    lb_info_title = Label(window,text="Thông tin nhà trọ",font="arial 20 bold  ",foreground="#053679",background="white")
    lb_info_content.place(x=100,y=300)
    lb_info_split = Label(window,text="",width=1,height=8,background="#053679")
    lb_info_name = Label(window,text="Tên trọ: Nhà trọ Python",font="arial 15 bold  ",background="white")
    lb_info_date = Label(window,text="Ngày lập: 15/7/2023",font="arial 15 bold  ",background="white")
    lb_info_des = Label(window,text="Mô tả: Nhà trọ giá sinh viên",font="arial 15 bold  ",background="white")
    lb_owner_name = Label(window,text="Tên chủ: Jenifer" ,font="arial 15 bold  ",background="white")
    lb_owner_phone = Label(window,text="SĐT: 0987654321",font="arial 15 bold  ",background="white")
    lb_info_address = Label(window,text="Địa chỉ: 273,An Dương Vương,P3,Q5",font="arial 15 bold  ",background="white")
    lb_bg = Label(window,image=bg)
    lb_bg.image = bg
    lb_bg.place(x=0,y=200)
    lb_info_title.place(x=280,y=0)
    lb_info_content.place(x=0,y=0)
    lb_info_split.place(x=425,y=50)
    lb_info_name.place(x=10,y=50)
    lb_info_date.place(x=10,y=100)
    lb_info_des.place(x=10,y=150)
    lb_owner_name.place(x=450,y=50)
    lb_owner_phone.place(x=450,y=100)
    lb_info_address.place(x=450,y=150)
    return window