import requests 
import numpy as np 
from time import sleep

#This is where we make the API Requests to the Server 
while True:
    response = requests.get("https://5204c28b7ad2.ngrok.io/SmokeData")
    sleep(1)
    print(response.json())

    a = response.json()

#Check out what data type there is: 
    print(type(a))

    print(a[1])
    print(a[2])
    print(a[0])
    if a[2] > 80.0:
        print("We got to this temperature\n")


