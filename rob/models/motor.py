################################################################################
#   motor.py
#
#   Motor Class on a base of GPIO Zero
#
#   Arguments:
#       side          - Left / Right Motor
#       forward_gpio  - Forward GPIO Pin connected to
#       backward_gpio - Forward GPIO Pin connected to
#       speed         - Motor speed    
#
#   13.07.2019  Created by:  zhenya
################################################################################
import gpiozero as GPIO

class Motor():
    def __init__(self, side, forward_gpio, backward_gpio, speed, factory):
        self.side          = side
        self.forward_gpio  = forward_gpio
        self.backward_gpio = backward_gpio
        self.speed         = speed

        self.motor_gpio  = GPIO.Motor(forward=self.forward_gpio, backward=self.backward_gpio, pin_factory=factory)
