import os
import sys
from bs4 import BeautifulSoup
import xlrd
import io

workbook = xlrd.open_workbook("C:\\Users\\yth2012\\Documents\\remediation_desc2.xls")
sheet = workbook.sheets()[0]

output = io.open("output.html", "w", encoding="utf-8")
col = 0
for row in range(sheet.nrows):
    output.write(sheet.cell(row,col).value)
output.close()

