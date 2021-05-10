import requests 
import numpy as np 
from time import sleep

#This is where we make the API Requests to the Server 
f = open("Data.txt", 'a')

#f.write("Now the file has more content! ")
c = 0
while c < 20:
    response = requests.get("http://d0f3b815bb46.ngrok.io/TempHumidData") 
    sleep(1)
    print(response.json())
    a = response.json()
    f.write(str(a[0]))
    f.write(",")
    f.write(str(a[1]))
    f.write(",")
    f.write(str(a[2]))
    f.write("/n")
    c = c+1

f.close()

##while c < 20:
##    response = requests.get("https://5204c28b7ad2.ngrok.io/SmokeData")
#    sleep(1)
#    print(response.json())
#
#    a = response.json()

#Check out what data type there is: 
#    print(type(a))

#    if a[1] > 100 : 
#        print ("We got this value ")
#    print(a[1])
#    print(a[2])
#    print(a[0])
#    f.write(str(a[0]))
#    f.write(" ,")
#    f.write(str(a[1]))
#    f.write(" ,")
#    f.write(str(a[2]))
#    f.write("\n")
#    c = c+1

#f.close()
