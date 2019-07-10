#!/usr/bin/env python3
################################################################################
#   rpi_gpio_demo.py
#
#   Demo samples for RPi.GPIO
#
#   03.07.2019  Created by: zhenya
################################################################################
import RPi.GPIO as GPIO
import time
from   pprint   import pprint

class RPiGPIODemo():
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.button_pin = 17
        self.led_pin    = 27
        
        GPIO.setup(self.button_pin, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def button_callback(self):
        led_blink()

    def button_event(self):
        GPIO.add_event_detect(self.button_pin,GPIO.RISING,callback=button_callback)

        message = input("Press enter to quit\n\n")
        GPIO.cleanup()

    def led_blink(self):    
        for i in range(4):
            GPIO.output(self.led_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.led_pin, GPIO.LOW)
            time.sleep(0.5)


