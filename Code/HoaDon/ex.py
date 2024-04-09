# file doc du lieu tu excel
from HoaDon.FormatHD import *
import pandas as pd
from pandas import ExcelFile
import os
cur_dir = os.path.abspath(".")
pd.options.display.max_rows = 9999

filehd = cur_dir + "/data/haodon.xlsx"
file=pd.read_excel(filehd)
file = file.fillna("")

lat = file.values.tolist()
list_hd=[]
for i in lat:
  c=Bill(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
  list_hd.append(c)

def getListBill():
  return list_hd