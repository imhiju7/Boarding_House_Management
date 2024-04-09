import openpyxl
import xlsxwriter
import os

cur_dir = os.path.abspath(".")
class Bill:
  def __init__(self, mahd,ngay,phong,tienphong,tinhtrang,dien,nuoc,xe,wifi,rac):
    self.mahd=mahd
    self.ngay = (ngay)
    self.phong = phong
    self.tienphong = tienphong
    self.tinhtrang = tinhtrang
    self.dien = dien
    self.nuoc = nuoc
    self.xe = xe
    self.wifi = wifi
    self.rac = rac
  def toString(self):
    return f"""
Mã:{self.mahd}
Ngày:{self.ngay} 
Phòng:{self.phong} 
Tiền phòng:{self.tienphong} đ
Tình trạng :{self.tinhtrang}
Điện :{self.dien} đ
Nước :{self.nuoc} đ
Wifi :{self.wifi} đ
Rác :{self.rac} đ
Tổng:{self.total()} đ
            """
  def total(self):
      s = str(int(self.tienphong) + int(self.dien) + int(self.nuoc) + int(self.xe) + int(self.wifi) + int(self.rac))
      return s
      
"""tạo file excel mới sau khi xóa"""
def new_excel(list_hd):
  workbook = xlsxwriter.Workbook(cur_dir + "/data/haodon.xlsx")
  worksheet = workbook.add_worksheet("My sheet")

  row = 0
  col = 0
  worksheet.write(row, col, "Mã hóa đơn")
  worksheet.write(row, col + 1, "Ngày")
  worksheet.write(row, col + 2, "phòng")
  worksheet.write(row, col + 3, "tiền phòng")
  worksheet.write(row, col + 4, "tình trạng")
  worksheet.write(row, col + 5, "điện")
  worksheet.write(row, col + 6, "nước")
  worksheet.write(row, col + 7, "xe")
  worksheet.write(row, col + 8, "wifi")
  worksheet.write(row, col + 9, "rác")
  row += 1
  for j in range (len(list_hd)):
    worksheet.write(row, col, list_hd[j].mahd)
    worksheet.write(row, col + 1, list_hd[j].ngay)
    worksheet.write(row, col + 2, list_hd[j].phong)
    worksheet.write(row, col + 3, list_hd[j].tienphong)
    worksheet.write(row, col + 4, list_hd[j].tinhtrang)
    worksheet.write(row, col + 5, list_hd[j].dien)
    worksheet.write(row, col + 6, list_hd[j].nuoc)
    worksheet.write(row, col + 7, list_hd[j].xe)
    worksheet.write(row, col + 8, list_hd[j].wifi)
    worksheet.write(row, col + 9, list_hd[j].rac)
    row += 1
  
  workbook.close()
