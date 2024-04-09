import tkinter as tk
from tkinter import*
from tkcalendar import *
from tkinter import ttk
from Phong import Phong
from tkinter import messagebox
from HoaDon import ex
from HoaDon import method
from HoaDon import FormatHD
import tree
#Đổ thông tin vào bảng chi tiết khi chọn dòng
def showBill(event):
    try:
        select = treeB.selection()[0]
        item = treeB.item(select)['values']
        
        en_b1.delete(0,END)
        en_b2.delete(0,END)
        en_b4.delete(0,END)
        en_b5.delete(0,END)
        en_b6.delete(0,END)
        en_b7.delete(0,END)
        en_b8.delete(0,END)
        en_b9.delete(0,END)
        
        for i in lstB:
            if i.mahd == item[0]:
                en_b1.insert(0,i.mahd)
                en_b2.insert(0,i.phong)
                en_b4.insert(0,i.tienphong)
                en_b5.insert(0,i.dien)
                en_b6.insert(0,i.nuoc)
                en_b7.insert(0,i.xe)
                en_b8.insert(0,i.wifi)
                en_b9.insert(0,i.rac)
                if (i.tinhtrang == "chua"):
                    rad1.select()
                else:
                    rad2.select()
                en_b3.selection_set(i.ngay)
    except IndexError:
        pass
#Xóa hóa đơn
def delBill():
    try:
        select = treeB.selection()[0]
        item = treeB.item(select)['values']
        value=str(en_b1.get())
        if (value != item[0]):
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
        for i in range(0,len(lstB)):
            if(item[0]==lstB[i].mahd):
                lstB.remove(lstB[i])
                t=1
                #Tạo mới file excel
                FormatHD.new_excel(lstB)
                break
        treeB.delete(select)
    except IndexError:
        pass
#Thêm hóa đơn
def addBill():
    value=str(en_b1.get())
    t=0
    k=""
    for i in range(0,len(lstB)):
        if(value == lstB[i].mahd):
            k=value
    for i in range(0,len(lstB)):
        if(value.startswith("HD") and value != k):
            t=1
            break
    if (method.check(str(en_b4.get()),str(en_b5.get()),str(en_b6.get()),str(en_b7.get()),str(en_b8.get()),str(en_b9.get()))) == False:
        t = 0
    if (t == 1):
        b =FormatHD.Bill(value,str(en_b3.get_date()),str(en_b2.get()),str(en_b4.get()),str(v_rad.get()),str(en_b5.get()),str(en_b6.get()),str(en_b7.get()),str(en_b8.get()),str(en_b9.get()))
        lstB.append(b)
        #Sau khi kiểm tra dữ liệu hợp lệ thì làm đổ danh sách vào file excel
        FormatHD.new_excel(lstB)
        treeB.insert('',END,values=(value,str(en_b2.get()),str(v_rad.get())))
    if(t==0):
        messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
def fixBill():
    try:
        if (method.check(str(en_b4.get()),str(en_b5.get()),str(en_b6.get()),str(en_b7.get()),str(en_b8.get()),str(en_b9.get()))) == False:
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
        select = treeB.selection()[0]
        data = treeB.item(select)["values"]
        value=str(en_b1.get())
        if (value != data[0]):
            messagebox.showinfo("Thông báo","Lỗi dữ liệu, hãy kiểm tra")
            return
        for i in range(len(lstB)):
            if lstB[i].mahd == value:
                lstB[i].ngay = str(en_b3.get_date())
                lstB[i].phong = str(en_b2.get())
                lstB[i].tienphong = int(en_b4.get())
                lstB[i].dien = int(en_b5.get())
                lstB[i].nuoc = int(en_b6.get())
                lstB[i].xe = int(en_b7.get())
                lstB[i].wifi = int(en_b8.get())
                lstB[i].rac = int(en_b9.get())
                lstB[i].tinhtrang = str(v_rad.get())
                
                FormatHD.new_excel(lstB)
                treeB.item(select,values=(value,lstB[i].phong,lstB[i].tinhtrang))
                return
    except IndexError:
        pass
#Frame chi tiết hóa đơn
def detailBillFrame(root):
    window = Frame(root,width=280,height=580,background="white")
    var_lstRoom = StringVar()
    ds = []
    for i in Phong.Room.toLstObj():
        ds.append(i.roomId)
    ds = tuple(ds)
    global en_b1,en_b2,en_b3,en_b4,en_b5,en_b6,en_b7,en_b8,en_b9,rad1,rad2,v_rad
    lb_b1 = Label(window,text="Mã HĐ: ",background="#FFF1DC")
    lb_b2 = Label(window,text="Phòng: ",background="#FFF1DC")
    lb_b3 = Label(window,text="Ngày: ",background="#FFF1DC")
    lb_b4 = Label(window,text="Giá phòng(đ): ",background="#FFF1DC")
    lb_b5 = Label(window,text="Tiền điện(đ): ",background="#FFF1DC")
    lb_b6 = Label(window,text="Tiền nước(đ):",background="#FFF1DC")
    lb_b7 = Label(window,text="Tiền xe(đ):",background="#FFF1DC")
    lb_b8 = Label(window,text="Wifi(đ): ",background="#FFF1DC")
    lb_b9 = Label(window,text="Tiền rác(đ):",background="#FFF1DC")
    en_b1 = Entry(window,background="#E8D5C4")
    en_b2 = ttk.Combobox(window,textvariable=var_lstRoom)
    en_b2['values'] = ds
    en_b3 = Calendar(window,selectmode = 'day',year = 2023,month=1,day = 1)
    en_b4 = Entry(window,background="#E8D5C4")
    en_b5 = Entry(window,background="#E8D5C4")
    en_b6 = Entry(window,background="#E8D5C4")
    en_b7 = Entry(window,background="#E8D5C4")
    en_b8 = Entry(window,background="#E8D5C4")
    en_b9 = Entry(window,background="#E8D5C4")
    v_rad = StringVar()
    rad1 = Radiobutton(window,text="Chưa đóng",variable=v_rad,value="chua")
    rad2 = Radiobutton(window,text="Đã đóng",variable=v_rad,value="da_dong")
    
    btn_b1 = Button(window,text="Thêm",width=10,command=addBill,background="#194485",fg="white")
    btn_b2 = Button(window,text="Xóa",width=10,command=delBill,background="#194485",fg="white")
    btn_b3 = Button(window,text="Sửa",width=10,command=fixBill,background="#194485",fg="white")
    
    lb_b3.place(x=120,y=0)
    lb_b1.place(x=20,y=210)
    lb_b2.place(x=20,y=240)
    lb_b4.place(x=20,y=270)
    lb_b5.place(x=20,y=300)
    lb_b6.place(x=20,y=330)
    lb_b7.place(x=20,y=360)
    lb_b8.place(x=20,y=390)
    lb_b9.place(x=20,y=420)
    
    en_b1.place(x=120,y=210)
    en_b2.place(x=120,y=240)
    en_b4.place(x=120,y=270)
    en_b5.place(x=120,y=300)
    en_b6.place(x=120,y=330)
    en_b7.place(x=120,y=360)
    en_b8.place(x=120,y=390)
    en_b9.place(x=120,y=420)
    
    en_b3.place(x=15,y=20)
    
    rad1.place(x=20,y= 450)
    rad2.place(x=120,y= 450)
    btn_b1.place(x=0,y=550)
    btn_b2.place(x=100,y=550)
    btn_b3.place(x=200,y=550)
    rad1.select()
    return window
#frame bảng dữ liệu hóa đơn
def tableBillFrame(root):
    window = Frame(root,width=650,height=280)
    global lstB,treeB
    lstB = ex.getListBill()
    treeB = tree.getTreeBill(window)
    treeB = tree.reload1(treeB)
    treeB.bind("<<TreeviewSelect>>", showBill)
    treeB.place(x=0,y=0)
    return window