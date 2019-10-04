# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "https://bmgxwpyyd2.execute-api.us-east-1.amazonaws.com/prod/sensordata"

# your source code here 
sensor_values = ''' 
{"temperature": 18,"humidity": 30}
'''
  
# data to be sent to api 
data = {'timestamp':'2019-10-03T17:05:00', 
        'sensorValues': sensor_values } 


r = requests.post(url = API_ENDPOINT, json = data) 

print("Data returned =%s"%r.text)