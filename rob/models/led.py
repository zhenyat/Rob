################################################################################
#   led.py
#
#   LED Class on a base of GPIO Zero
#
#   Arguments:
#       color - LED Color
#       gpio  - GPIO Pin LED connected to
#
#   10.07.2019  Created by:  zhenya
################################################################################
import gpiozero as GPIO

class LED():
    def __init__(self, color, gpio, factory):
        self.color = color
        self.gpio  = gpio

    def get(self):
        print(self.color, self.gpio)
        
    def blink(self):
        pass
    
    def light_off(self):
        pass

    def light_on(self):
        pass


    