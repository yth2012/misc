import requests
from bs4 import BeautifulSoup
import csv


try:
    htmlfile = open("douban.html","r")
    html = htmlfile.read()

except:
    url = "http://movie.douban.com/cinema/later/shenzhen/"

    res = requests.get(url)
    htmlfile = open("douban.html","w")

    html = res.content.decode("utf-8")
    htmlfile.write(html)
    htmlfile.close()

soup = BeautifulSoup(html,'lxml')
allmv = soup.find("div",id="showing-soon")
movies = allmv.find_all("div",class_="mod")


resultcsv = open("result.csv","w",encoding="gbk",newline="\n")
wr = csv.writer(resultcsv)
arow = ["name","link","date","category","region"]
wr.writerow(arow)


for m in movies:
    name = m.find("a",class_="").text
    link = m.find("a",class_="")["href"]
    info = m.find_all("li")
    date = info[0].text
    cat = info[1].text
    reg = info[2].text
    wr.writerow([name,link,date,cat,reg])

resultcsv.close()

   

        




