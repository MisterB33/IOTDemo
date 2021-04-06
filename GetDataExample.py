import requests 
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np 


#This is where we make the API Requests to the Server 

response = requests.get("http://cef7bc227677.ngrok.io/TempHumidData")

print(response.json())

a = response.json()

#Check out what data type there is: 

print(type(a))

print(a[1])
print(a[2])
print(a[0]) 


