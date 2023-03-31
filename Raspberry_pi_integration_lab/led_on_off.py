 #Import GPIO Library
import RPi.GPIO as GPIO
#Import time function Library
import time
#Configure GPIO in Raspberry Pi BCM Mode
GPIO.setmode(GPIO.BCM) 
#Configure GPIO Pin 17 as output
GPIO.setup(17,GPIO.OUT) 
#set loop for 5 blinks
a=0
while a<=5:
 #Set GPIO Pin to High
 GPIO.output(17,GPIO.HIGH)
 #Wait for 1sec
 time.sleep(1)
 #Set GPIO Pin to Low
 GPIO.output(17,GPIO.LOW)
 time.sleep(1)
a+=1
