################################################################################
#   zt_rpi_gpio.py
#
#   Gfround for RPi.GPIO
#
#   03.07.2019  Created by: zhenya
################################################################################
import RPi.GPIO as GPIO
import time
from pprint import pprint

class ZtRPiGPIO():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        set_objects()
        
    def set_objects(self):
        

