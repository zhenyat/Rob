################################################################################
#   button.py
#
#   Button Class on a base of GPIO Zero
#
#   Arguments:
#       name    - Button Name
#       color   - Button Color
#       gpio    - GPIO Pin Button connected to
#       factory - GPIO Pins Factory
#
#   10.07.2019  Created by:  zhenya
################################################################################
import gpiozero as GPIO

class Button():
    def __init__(self, name, color, gpio, factory):
        self.name  = name
        self.color = color
        self.gpio  = gpio

        # Assigns GPIO pin to the Button
        self.button_gpio = GPIO.Button(self.gpio, pin_factory=factory)

    def get_attr(self):
        return(self.name, self.color, self.gpio)

    def is_pressed(self):
        if (self.button_gpio.is_pressed): return(True)
        else:                             return(False)