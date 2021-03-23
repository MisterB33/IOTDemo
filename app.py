from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
#from nanpy import DHT,ArduinoApi,SerialManager 
import Sensors
import serial 

app = Flask(__name__) #initializing flask app class

ser = serial.Serial('/dev/ttyACM0',9600) #establishing the connection on a specific serial port

@app.route('/', methods=["GET", "POST"])
def main():
	return render_template('index.html')


@app.route('/TempHumidData', methods=["GET", "POST"]) #Posting Data to graphs and guages
def data(ser=ser):
# Data Format
# [TIME, Temperature, Humidity]
	temp = Sensors.ReadDHT11(ser)#dht.readtemperature(True)    		# Printing resultant string 
	print(temp[0])
	print(temp[1])
	data = [time() * 1000, float(temp[0]),float(temp[1])]
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
    		
	return response
@app.route('/SoundData',methods=["GET","POST"]) 
def soundData(ser = ser):
	temp = 10.0 
	print(temp)
	data = [temp,float(4.0)] 
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response 


@app.route('/SmokeData',methods=["GET","POST"]) 
def smokeData(ser = ser):
	temp = 10.0 
	print(temp)
	data = [temp,float(4.0)] 
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response 


@app.route('/LightData',methods=["GET","POST"]) 
def lightData(ser = ser):
	temp = 10.0 
	print(temp)
	data = [temp,float(4.0)] 
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response 

@app.route('/PressureData',methods=["GET","POST"]) 
def pressureData(ser = ser):
	temp = 10.0 
	print(temp)
	data = [temp,float(4.0)] 
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response 


@app.route('/AirQualityData',methods=["GET","POST"]) 
def AirQualityData(ser = ser):
	temp = 10.0 
	print(temp)
	data = [temp,float(4.0)] 
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response 

if __name__ == "__main__":
    app.run(debug=True)
