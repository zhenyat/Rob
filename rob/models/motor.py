################################################################################
#   motor.py
#
#   Motor Class on a base of GPIO Zero
#
#   Arguments:
#       kind          - Left / Right Motor
#       forward_gpio  - Forward GPIO Pin connected to
#       backward_gpio - Forward GPIO Pin connected to
#       speed         - Motor speed    
#
#   10.07.2019  Created by:  zhenya
################################################################################
import time

class Motor():
    def __init__(self, kind, forward_gpio, backward_gpio, speed):
        self.kind          = kind
        self.forward_gpio  = forward_gpio
        self.backward_gpio = backward_gpio
        self.speed         = speed

