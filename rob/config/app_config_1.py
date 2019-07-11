################################################################################
#   app_config.py
#
#   App configuration:
#       - reads input data
#       - tests connection to Raspberry Pi
#
#   22.06.2019  Created by: zhenya
#   10.07.2019  Update: new data structure of LEDs & Buttons
################################################################################
import os
import sys
import yaml

import gpiozero             as     GPIO
from   gpiozero.pins.pigpio import PiGPIOFactory

from   controllers.gpio     import *
from   lib.tools            import *
from   models.button        import *
from   models.host          import *
from   models.led           import *

class AppConfig():
    def __init__(self):
        self.buttons = []
        self.leds    = []
        
        params = self.read_values()

        self.initialize_host(params)
        self.initialize_models(params)
        for led in self.leds:
            led.get()
        for button in self.buttons:
            button.get()
        sys.exit('debug STOP')
        
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

    # Initializes Host according to yml-data
    def initialize_host(self, params):
        self.host_addr = params['host']['addr']
        self.host_name = params['host']['name']
        self.host_user = params['host']['user']
        
        if params['host']['test']: 
            log("Testing connection to Raspberry Pi...")
            self.test_connection()
                
        self.factory = PiGPIOFactory(host=self.host_addr)
        GPIO.Device.pin_factory = self.factory            # Workaround: MUST BE!!!

#        self.debug = params['debug']
#        self.demo  = params['demo']

    # Initializes Models according to yml-data
    def initialize_models(self, params):
        
        if ('buttons') in params:
            for button in params['buttons']:
                self.buttons.append(Button(button['name'], button['color'], button['gpio']))
            else:
                log('No Buttons to be initialized')

        if ('leds') in params:
            for led in params['leds']:
                self.leds.append(LED(led['color'], led['gpio']))
        else:
            log('No LEDs to be initialized')

    # Verifies connection with Raspberry Pi
#    def test_connection(self):
#        response  = os.system("ping -c 1 " + self.host_addr)
#        if response == 0:
#            log('Connection is OK')
#        else:
            sys.exit('Connection failed')
