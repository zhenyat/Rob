################################################################################
#   app_config.py
#
#   App configuration:
#       - reads input data
#       - tests connection to Raspberry Pi
#
#   22.06.2019  Created by: zhenya
################################################################################
import os
import sys
import yaml

import gpiozero             as     GPIO
from   gpiozero.pins.pigpio import PiGPIOFactory

from   controllers.gpio     import *
from   lib.tools            import *

class AppConfig():
    def __init__(self):
        params = self.read_values()

        self.host_addr = params['host']['addr']
        self.host_name = params['host']['name']
        self.host_user = params['host']['user']
        
        if params['host']['test']: 
            log("Testing connection to Raspberry Pi...")
            self.test_connection()
                
        self.factory = PiGPIOFactory(host=self.host_addr)
        GPIO.Device.pin_factory = self.factory            # Workaround: MUST BE!!!

        self.debug = params['debug']
        self.demo  = params['demo']
        
        # GPIO pins
        self.button_gpio = params['button']['gpio']
        self.led_gpio    = params['led']['gpio']
        self.pigpio_gpio = params['pigpio']['gpio']

        self.motor_left_forward   = params['motors']['left']['forward_gpio']
        self.motor_left_backward  = params['motors']['left']['backward_gpio']
        self.motor_right_forward  = params['motors']['right']['forward_gpio']
        self.motor_right_backward = params['motors']['right']['backward_gpio']

        self.motor_speed = params['motors']['speed']
        
    # Reads yml-file with input data
    def read_values(self, file_name='config/params.yml'):
        with open(file_name, 'r') as stream:
            try:
                return(yaml.safe_load(stream))          # Return Dictionary
            except yaml.YAMLError as error_message:
                log(error_message)
                sys.exit("Failed to read params")

    # Verifies connection with Raspberry Pi
    def test_connection(self):
        response  = os.system("ping -c 1 " + self.host_addr)
        if response == 0:
            log('Connection is OK')
        else:
            sys.exit('Connection failed')
