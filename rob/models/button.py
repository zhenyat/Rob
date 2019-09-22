################################################################################
#   button.py
#
#   Button Class nheriting GPIO Zero LED class
#
#   Ref:    gpiozero_1.5.0.pdf, p. 97
#
#   Child class arguments:
#       name  - Button Name
#       color - Button Color

#   22.09.2019  Created by:  zhenya
################################################################################
import gpiozero

class Button(gpiozero.Button):
    def __init__(self, gpio, pin_factory, name='Dummy', color='red'):
        self.name  = name
        self.color = color
        super().__init__(pin=gpio, pin_factory=pin_factory)

