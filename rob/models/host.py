################################################################################
#   host.py
#
#   Class Host
#
#   Arguments:
#       addr  - IP Address
#       name  - Host Name
#       user  - User (login)
#
#   10.07.2019  Created by:  zhenya
################################################################################
import os
import sys

import gpiozero             as     GPIO
from   gpiozero.pins.pigpio import PiGPIOFactory

from   lib.tools import *

class Host():
    def __init__(self, addr, name, user):
        self.addr = addr
        self.name = name
        self.user = user

        self.factory = PiGPIOFactory(host=self.addr)
        GPIO.Device.pin_factory = self.factory         # Workaround: MUST BE!!!

