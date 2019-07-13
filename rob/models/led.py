################################################################################
#   led.py
#
#   LED Class on a base of GPIO Zero
#
#   Arguments:
#       color   - LED Color
#       gpio    - GPIO Pin LED connected to
#       factory - GPIO Pins Factory
#
#   10.07.2019  Created by:  zhenya
################################################################################
import gpiozero as GPIO

class LED():
    def __init__(self, color, gpio, factory):
        self.color   = color
        self.gpio    = gpio
        self.factory = factory

        # Assigns GPIO pin to the LED
        self.led_gpio = GPIO.LED(self.gpio, pin_factory=self.factory)

    def get_attr(self):
        return(self.color, self.gpio)
        
    def is_color(self, color):
        if self.color == color: return(True)
        else:                   return(False)
        
    def blink(self, times=5):
        self.led_gpio.blink(n=times, background=False)
    
    def off(self):
        self.led_gpio.off()

    def on(self):
        self.led_gpio.on()
        pass

    