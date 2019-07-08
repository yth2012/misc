
try:
    myfile = open("afile.txt","a+")

except:
    myfile = open("afile.txt","w")

myfile.seek(0)
l = myfile.readline()
print(l)
myfile.seek(2)
myfile.write("second line\n")


myfile.close()

