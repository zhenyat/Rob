#!/usr/bin/env python3
################################################################################
#   01_ir_led_test.py
#
#   First test of IR Remote with LED
#   Different pults can be tested
#
#   29.06.2019  Created by:  zhenya
################################################################################
import RPi.GPIO as GPIO
import time

IR_pin  = 40	# Physical pin no (GPIO21)  Default is GPIO18 under LIRC?
LED_pin = 13	# Physical pin no (GPIO27)

def setup():
	GPIO.setmode(GPIO.BOARD)       # GPIO Numbers by PHYSICAL pins
	GPIO.setup(IR_pin,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(LED_pin, GPIO.OUT)

def counter(ev=None):
	global count
	count += 1
	print('Received infrared. count = ', count)
	GPIO.output(LED_pin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(LED_pin, GPIO.LOW)

def loop():
	GPIO.add_event_detect(IR_pin, GPIO.FALLING, callback=counter) # wait for falling
	while True:
		pass               # Do nothing
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		print('===== Ctrl C')
	except:
		print('===== Error, etc.')
	finally:
		GPIO.cleanup()
