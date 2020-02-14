import time 
import serial
import binascii
import json
import datetime
import requests
     
ser = serial.Serial( "/dev/ttyS0", baudrate = 9600)
API_ENDPOINT = "https://bmgxwpyyd2.execute-api.us-east-1.amazonaws.com/prod/sensordata"

while 1:
    i = 0
    buffer = []
    
    macaddress = []
    sensordata1 = []
    sensordata2 = []
    while i < 24:
        
        buffer.append(ser.read())
    
        if (i>=4 and i<=11):
            macaddress.append(buffer[i])  
        if (i == 19 or i == 20):
            sensordata1.append(buffer[i])
        if (i == 21 or i == 22):
            sensordata2.append(buffer[i])

        i +=1
    
    address = macaddress[0] + macaddress[1] + macaddress[2] + macaddress[3] + macaddress[4] + macaddress[5] + macaddress[6] + macaddress[7]
    addresshex = binascii.hexlify(address).decode("utf-8")
    
    sensor1 = sensordata1[0] + sensordata1[1]
    sensor1 = int.from_bytes(sensor1, byteorder= 'big')
    
    sensor2 = sensordata2[0] + sensordata2[1]
    sensor2 = int.from_bytes(sensor2, byteorder= 'big')
    
    #print("Raw Packet:")
    #print(buffer)
    #print("MacAddress:")
    #print(addresshex)
    #print("Sensor1:")
    #print(sensor1)
    #print("Sensor2:")
    #print(sensor2)
    #print("\n")
    
    if(addresshex == "0013a20041a59768"):
        sensor = {"ROUTER1_SENSOR1": str(sensor1),
                  "ROUTER1_SENSOR2": str(sensor2)}
     
    if(addresshex == "0013a20041052fbf"):
        sensor = {"ROUTER2_SENSOR1": str(sensor1),
                  "ROUTER2_SENSOR2": str(sensor2)}
        
    data = {
            "timestamp": "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()),
            "sensorValues": json.dumps(sensor)
        }
    
    #post request
    postdata = data
    r = requests.post(url = API_ENDPOINT, json = postdata)
    print("Data returned =%s"%r.text)