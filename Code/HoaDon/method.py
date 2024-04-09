from HoaDon.FormatHD import *
from HoaDon.ex import *
import pandas as pd
from pandas import ExcelFile
pd.options.display.max_rows = 9999
from tkinter import *

def check(money:str,dien:str,nuoc:str,xe:str,wifi:str,rac:str):
    if money.isdigit()==False:
        return False
    if dien.isdigit()==False:
        return False
    if nuoc.isdigit()==False:
        return False
    if xe.isdigit()==False:
        return False
    if wifi.isdigit()==False:
        return False
    if rac.isdigit()==False:
        return False
    return True
    