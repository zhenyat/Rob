################################################################################
#   motor.py
#
#   Motor class inheriting GPIO Zero Motor class
#
#   Ref:    gpiozero_1.5.0.pdf, p. 120
#
#   Child class arguments:
#       color   - Motor Color
#
#   22.09.2019  Created by:  zhenya
################################################################################
import gpiozero

class Motor(gpiozero.Motor):
    def __init__(self, forward_gpio, backward_gpio, pin_factory, side, speed):
        self.side  = side
        self.speed = speed 
        super().__init__(forward=forward_gpio, backward=backward_gpio, pin_factory=pin_factory)
