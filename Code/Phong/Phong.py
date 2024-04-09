import openpyxl
import pandas
from tkinter import messagebox
from tkinter import *
import os
cur_dir = os.path.abspath(".")
file_Khach= pandas.read_excel((cur_dir + "/data/data.xlsx"),sheet_name='khach') 
file_Khach=file_Khach.fillna("")
cuslist=file_Khach.values.tolist()


file_Phong= pandas.read_excel((cur_dir + "/data/data.xlsx"),sheet_name='phong') 
file_Phong=file_Phong.fillna("")
roomlist=file_Phong.values.tolist()
class Room: 
    def __init__(self, roomId, square, status, maxPeople) :
        self.roomId = roomId
        self.square = square
        self.status = status
        self.maxPeople = maxPeople
    def getRoomID(self):
        return self.roomId
    def getSQ(self):
        return self.square
    def getStatus(self):
        return self.status
    def getMaxP(self):
        return self.maxPeople
    def getlstCus(self):
        s = ""
        for i in cuslist:
            if i[4] == self.roomId:
                s += i[0] + "\n"
        return s;
    def toLstObj():
        lst = []
        for i in roomlist:
            r = Room(i[0],i[1],i[2],i[3])
            lst.append(r)
        return lst
    def getLstEmpty():
        lst = Room.toLstObj()
        lst2 = []
        for i in lst:
            if i.status == "trong":
                lst2.append(i)
        return lst2
def checkRInfo(id : str,sq:str,mp:str):
    if id.startswith("P") == False:
        return False
    try:
        float(sq)
    except ValueError:
        return False
    if mp.isdigit() == False:
        return False
    return True