from ftplib import FTP
import sys

def writetofile(data):
    try:
        file = open("ftpfile","wb")
    except:
        exit("file open err")

    file.write(bytes(data,encoding="utf-8"))
    file.close()


try:
    host, login, pw = sys.argv[1],sys.argv[2], sys.argv[3]
except IndexError:
    exit("not enoug arg")

ftp = FTP(host)
ftp.login(login, pw)

ftp.retrlines("RETR vsftpd_vuser.db",callback=writetofile)