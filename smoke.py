import RPi.GPIO as GPIO
import time

#GPIO Setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback (channel):
    if GPIO.input(channel):
        print("dangerous gass detected")
    else:
        print("no dangerous gas detected")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #let us know if the pin goes high or low
GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN, Run the function on change

#Infinite loop
while True:
    time.sleep(1)
