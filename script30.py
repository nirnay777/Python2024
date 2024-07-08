import os
reclen = 20
size = os.path.getsize('cities.bin')
totalRecords = int(size/reclen)

f1 = open('cities.bin','rb')
f2 = open('cities.bin','wb')

cityToBeDeleted = input('enter the city to be deleted')
cityToBeDeleted = cityToBeDeleted + (reclen - len(cityToBeDeleted)) * " "
cityToBeDeleted = cityToBeDeleted.encode()

for x in range(totalRecords):
    str = f1.read(reclen)
    if(cityToBeDeleted != str):
        f2.write(str)
f1.close()
f2.close()
os.remove('cities.bin')
os.rename('cities2.bin','cities.bin')

str = "nirnay:7263880368"
info = "nirnay - sangolkar - 20/10/2001"
print(str.split(":")[1])
print(info.split("-")[2])
