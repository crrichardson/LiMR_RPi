import RPi.GPIO as GPIO
    
def button_callback(channel):  # define function 
    print("Button was pressed!") # print message

GPIO.setwarnings(False) # not using warnings
GPIO.setmode(GPIO.BOARD) #Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set pin10 as input, set initial value as low

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback) #set event on pin10 rising edge

message = input("enter to exit\n\n") # Runs until you press enter
GPIO.cleanup()