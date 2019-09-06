import xml
import xlrd
from html.parser import HTMLParser
import io
import sys

class myparser(HTMLParser):
    
    '''def handle_starttag(self,tag,attrs):
        print("<{}>".format(tag))'''

    def handle_data(self,data):
        if self.get_starttag_text() in ["<p>", "<xhtml:p>"]: 
            if data.strip():
                global cnt
                print("{}:{} <data> {}".format(roww,cnt,data))
                cnt += 1
            else:
                print("<null>")

    '''def handle_endtag(self, tag):
        print("</{}>".format(tag))'''
    
    '''def handle_startendtag(self,tag,attrs):
        print("a empty tag {}".format(tag))'''

workbook = xlrd.open_workbook("C:\\Users\\yth2012\\Documents\\remediation_desc2.xls")
sheet = workbook.sheets()[0]
par = myparser()


txt = []
col = 0
for row in range(sheet.nrows):
    txt.append(sheet.cell(row,col).value)

roww = 0
cnt = 0

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
for i in txt:
    par.feed(i)
    roww += 1
    cnt = 0
    




