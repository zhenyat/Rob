################################################################################
#   button.py
#
#   Button Class on a base of GPIO Zero
#
#   Arguments:
#       name  - Button Name
#       color - Button Color
#       gpio  - GPIO Pin Button connected to
#
#   10.07.2019  Created by:  zhenya
################################################################################
import gpiozero as GPIO

class Button():
    def __init__(self, name, color, gpio, factory):
        self.name  = name
        self.color = color
        self.gpio  = gpio
        
        GPIO.Button(self.gpio, pin_factory=factory)

    def get(self):
        print(self.name, self.color, self.gpio)

#        self.button = GPIO.Button(config.button_gpio, pin_factory=config.factory)
