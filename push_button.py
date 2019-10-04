import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #USe physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set pin10 as input, set initial value as low

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Button pressed!")