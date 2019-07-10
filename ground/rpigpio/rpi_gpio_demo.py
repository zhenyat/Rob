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

button_pin = 17
led_pin    = 27
    
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(led_pin, GPIO.OUT)

def button_callback(button_pin):
    led_blink()

def button_event():
    GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback)

    message = input("Press enter to quit\n\n")
    GPIO.cleanup()

def check_button():
    for i in range(4):
        print(GPIO.input(button_pin))
        time.sleep(2)
    
def led_blink():    
    for i in range(4):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)

init()
check_button()
#button_event()
