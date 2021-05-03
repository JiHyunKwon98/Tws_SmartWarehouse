#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# SimpleMFRC522 객체 생성
reader = SimpleMFRC522()

try:
    while True:
    	text = input("Text:")
    	print("Please contact your card")
    	reader.write(text)
    	print("Complete!")
finally:
	GPIO.cleanup()