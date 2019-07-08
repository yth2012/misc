import requests
from bs4 import BeautifulSoup


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


resulthtml = open("result.html","w", encoding="utf-8")
resulthtml.write('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>movies</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
<h2 class="text-center">movies</h2>
<table class="table table-striped table-hover mx-auto text-center">
    <thead>
        <tr>
            <th>name</th>
            <th>date</th>
            <th>category</th>
            <th>region</th>
        </tr>
    </thead>
    <tbody>
''')

for m in movies:
    name = m.find("a",class_="").text
    link = m.find("a",class_="")["href"]
    info = m.find_all("li")
    date = info[0].text
    cat = info[1].text
    reg = info[2].text

    resulthtml.write('''
    <tr>
        <th><a href="{}">{}</th>
        <th>{}</th>
        <th>{}</th>
        <th>{}</th>
    </tr>
    '''.format(link, name, date, cat, reg))

resulthtml.write('''
</tbody>
</table>
</body>
</html>
''')
resulthtml.close()

        




