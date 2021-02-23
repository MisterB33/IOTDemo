from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
from nanpy import DHT,ArduinoApi,SerialManager 
import TempHumid
import serial 

app = Flask(__name__) #initializing flask app class

ser = serial.Serial('/dev/ttyUSB0',9600) #establishing the connection on a specific serial port


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"]) #Posting Data to graphs and guages
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
    temp = TempHumid.ReadDHT11(ser)#dht.readtemperature(True) 
    # Printing resultant string 
    print(temp[0])
    print(temp[1])
    data = [time() * 1000, float(temp[0]),float(temp[1])]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
