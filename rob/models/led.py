################################################################################
#   led.py
#
#   LED class inheriting GPIO Zero LED class
#
#   Ref:    gpiozero_1.5.0.pdf, p. 115
#
#   Child class arguments:
#       color   - LED Color
#
#   22.09.2019  Created by:  zhenya
################################################################################
import gpiozero

class LED(gpiozero.LED):
    def __init__(self, gpio, pin_factory, color='red'):
        self.color = color
        super().__init__(pin=gpio, pin_factory=pin_factory)
