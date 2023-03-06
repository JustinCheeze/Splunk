import RPi.GPIO as GPIO
from time import sleep

smoke = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(smoke,GPIO.IN)


try:
       while True:

             x = GPIO.input(smoke)
             time.sleep(0.03)

           
except KeyboardInterrupt:
    GPIO.cleanup()
