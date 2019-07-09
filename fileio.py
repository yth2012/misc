
try:
    myfile = open("afile.txt","r+")

except:
    myfile = open("afile.txt","w")

'''myfile.seek(0)
l = myfile.readline()
print(l)
myfile.seek(2)
myfile.write("second line\n")


myfile.close()'''

for fn in myfile:
    print(fn)

