from tkinter import ttk
import tkinter as tk
from HoaDon import ex
from Khach import pytoex
from HoaDon.FormatHD import Bill
from Phong import Phong

# Các hàm trả về treeview
def getTreeBill(win):
    bill_col = ('id','room','status')
    tree_bill = ttk.Treeview(win,height=12 ,columns=bill_col, show='headings')
    tree_bill.column('id',width=100)
    tree_bill.column('room',width=250)
    tree_bill.column('status',width=300)
    tree_bill.heading('id', text='Mã')
    tree_bill.heading('room', text='Phòng')
    tree_bill.heading('status', text='Tình trạng')
    return tree_bill

def getlstCD():
    lst = ex.getListBill()
    newLst = []
    for i in lst:
        if i.tinhtrang == "chưa":
            newLst.append(i)
    return newLst
def getTB2(win):
    bill_col = ('id','room','status')
    tree_bill = ttk.Treeview(win,height=12 ,columns=bill_col, show='headings')
    tree_bill.column('id',width=100)
    tree_bill.column('room',width=250)
    tree_bill.column('status',width=300)
    tree_bill.heading('id', text='Mã')
    tree_bill.heading('room', text='Phòng')
    tree_bill.heading('status', text='Tình trạng')
    return tree_bill
def reload1(tree_bill: ttk.Treeview):
    lst = ex.getListBill()
    data = []
    for i in tree_bill.get_children():
        tree_bill.delete(i)
    for i in lst:
        data.append((f"{i.mahd}",f"{i.phong}",f"{i.tinhtrang}"))
    for i in data:
        tree_bill.insert('', tk.END, values=i)
    return tree_bill
def reload2(tree_bill: ttk.Treeview):
    lst = getlstCD()
    data = []
    for i in tree_bill.get_children():
        tree_bill.delete(i)
    for i in lst:
        data.append((f"{i.mahd}",f"{i.phong}",f"{i.tinhtrang}"))
    for i in data:
        tree_bill.insert('', tk.END, values=i)
    return tree_bill
def getTC(win):
    cus_col = ('id','name','room','phone')
    tree_cus = ttk.Treeview(win,height=12 ,columns=cus_col, show='headings')
    tree_cus.column('id',width=100)
    tree_cus.column('name')
    tree_cus.column('room',width=150)
    tree_cus.column('phone')
    tree_cus.heading('id', text='Mã')
    tree_cus.heading('name', text='Tên')
    tree_cus.heading('room', text='Phòng')
    tree_cus.heading('phone', text='sdt')
    return tree_cus
def reload3(tree:ttk.Treeview):
    lst = pytoex.getlst()
    data = []
    for i in tree.get_children():
        tree.delete(i)
    for i in lst:
        data.append((i[3],i[0],i[4],i[2]))
    for i in data:
        tree.insert('','end',values=i)
    return tree
def getRT(win):
    r_col = ('id','sq','status','max')
    tree_r = ttk.Treeview(win,height=12 ,columns=r_col, show='headings')
    tree_r.column('id',width=100)
    tree_r.column('sq')
    tree_r.column('status',width=150)
    tree_r.column('max')
    tree_r.heading('id', text='Mã')
    tree_r.heading('sq', text='Diện tích')
    tree_r.heading('status', text='Trạng thái')
    tree_r.heading('max', text='Số người max')
    return tree_r
def reload4(tree:ttk.Treeview):
    lst = Phong.Room.toLstObj()
    data = []
    for i in tree.get_children():
        tree.delete(i)
    for i in lst:
        data.append((i.roomId,i.square,i.status,i.maxPeople))
    for i in data:
        tree.insert('','end',values=i)
    return tree