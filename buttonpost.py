import RPi.GPIO as GPIO

# importing the requests library 
import requests
import time
from datetime import datetime


# defining the api-endpoint 
API_ENDPOINT = "https://bmgxwpyyd2.execute-api.us-east-1.amazonaws.com/prod/sensordata"


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #USe physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set pin10 as input, set initial value as low

while True:
    sensor_values = ''' 
    {"button": 0 }
    '''
    if GPIO.input(10) == GPIO.HIGH:
        sensor_values = ''' 
        {"button": 1}
        '''

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # data to be sent to api 
    data = {'timestamp': timestamp, 
            'sensorValues': sensor_values } 


    r = requests.post(url = API_ENDPOINT, json = data) 
    time.sleep(1)