#!/usr/bin/python
import RPi.GPIO as GPIO
import platform
import sys
import datetime
import json
import platform
import random
import pymongo
import socket
import time
import picamera
import time
from pymongo import MongoClient

time.sleep(60) # 1 minute to boot up

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(11, GPIO.OUT)       #LED output pin

colors = [0xFF00, 0x00FF]
pins = {'pin_R':10, 'pin_G':11}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
	GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output


p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def setColor(col):
	R_val = (col & 0xFF00) >> 8
	G_val = (col & 0x00FF) >> 0
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(G_val)

try:
    while True:
        #k=0
        i=GPIO.input(7)
        if i==0:                 #When output from motion sensor is LOW
            print( "No intruders",i)
            setColor(0x00FF)
            GPIO.output(11, 1)  #Turn ON LED - GREEN - all good
        elif i==1: 
            #k=1              #When output from motion sensor is HIGH
            print ("Intruder detected",i)
            setColor(0xFF00)
            GPIO.output(11, 1)  #Turn ON LED - RED - intruder
            #from picamera import PiCamera from time import sleep 
            camera = picamera.PiCamera() 
            #camera.start_preview() 
            picpath = '/home/pi/Desktop/'+str(datetime.datetime.now())+'.jpg'
            camera.capture(picpath) 
            time.sleep(2)
            #camera.stop_preview()   
            camera.close()    
        time.sleep(3) # wait for 10 seconds before trying again on 
except KeyboardInterrupt:
    p_R.stop()
    p_G.stop()
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
    GPIO.cleanup()
