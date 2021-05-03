#! /usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from board import SCL, SDA
import busio
from adafruit_pca9685 import adafruit_pca9685
from adafruit_motor import servo

# create pca9685 instance
i2c = busio.I2C(SCL, SDA)

# create a simple PCA9685 class instance.
pca = PCA9685(i2c)

# set pwm signal frequency 50Hz
pca.frequency = 50

# servo motor channel 6 and 7
# attribute : fraction(0.0 ~ 1.0), angle(0 ~ 180)
servo6 = servo.ContinuousServo(pca.channels[7])
servo7 = servo.ContinuousServo(pca.channels[6])

# led attribute : duty_cycle(0x0000 ~ 0xffff)
led0 = pca.channels[0]
led1 = pca.channels[1]

# create 'SimpleMFRC522' object
reader = SimpleMFRC522()

try:
	while True:
		id, text = reader.read()
		print("your RFID tag is {}".format(text))
		if "A3" in text:
			led1.duty_cycle = 0xffff
			led0.duty_cycle = 0x0000
			servo7.fraction = 0.7
			time.sleep(3)
			servo7.fraction = 0.5
		elif "A1" in text:
			led1.duty_cycle = 0x0000
			led0.duty_cycle = 0xffff
			servo6.fraction = 0.7
			time.sleep(3)
			servo6.fraction = 0.5
		else :
			led1.duty_cycle = 0x0000
			led0.duty_cycle = 0x0000
			time.sleep(1)
finally:
    pca.deinit()