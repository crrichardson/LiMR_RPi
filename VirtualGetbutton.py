import RPi.GPIO as GPIO

# importing the requests library 
import requests
import json
import time
from datetime import datetime


# defining the api-endpoint 
API_ENDPOINT = "https://bmgxwpyyd2.execute-api.us-east-1.amazonaws.com/prod/sensordata"
pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #USe physical pin numbering
GPIO.setup(pin, GPIO.OUT)






while True:
#    print('LED offf')
#    GPIO.output(pin,GPIO.LOW)
#    time.sleep(0.1)
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    sensor_values = ''' 
    {"button": 0 }
    '''
    
  
    
    g = requests.get(url = API_ENDPOINT, params = sensor_values)
    data = g.json()
    
    switch = data['sensorValues']
    ledtemp = json.loads(switch)
    final = ledtemp['led1']
    
    print (ledtemp['led1'])
    
    if final == '1':
        GPIO.output(pin,GPIO.HIGH)
        
    elif final == '0':
        GPIO.output(pin,GPIO.HIGH)
        
    else:
        print ('Unknown Value')
    
    time.sleep(0.1)
    
    

    #if :
    #  GPIO.input(10) == GPIO.HIGH  sensor_values = ''' 
     #   {"button": 1}
     #   '''

    #timestamp = datetime.timestamp(now)
    # data to be sent to api 
    #data = {'timestamp': timestamp, 
    #        'sensorValues': sensor_values } 


    #r = requests.post(url = API_ENDPOINT, json = data) 
    #time.sleep(0.1)

