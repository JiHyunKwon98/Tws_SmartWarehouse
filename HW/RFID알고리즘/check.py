#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# SimpleMFRC522 객체 생성
reader = SimpleMFRC522()

# example UID number : D3 A8 BC 02 C5
id1 = 0xD3A8BC02C5

GPIO.setmode(GPIO.BOARD)  # GPIO의 사용할 pin Mode 설정
                          # BCM : GPIO 번호, BOARD : 물리적번호
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

try:
	while True:
		id, text = reader.read()  # UID와 text를 모두 읽음
        if id == id1:
        	GPIO.output(5, False)
        	GPIO.output(7, True)
        else:
        	GPIO.output(5, True)
        	GPIO.output(7, False)
finally:
	GPIO.cleanup()