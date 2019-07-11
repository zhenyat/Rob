################################################################################
#   app_config.py
#
#   App configuration:
#       - reads input data
#       - tests connection to Raspberry Pi
#
#   22.06.2019  Created by: zhenya
#   10.07.2019  Update: new data structure of LEDs, Buttons, etc
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
#        self.buttons = []
#        self.leds    = []
#        self.motors  = []
        
        params = self.read_values()

        self.initialize_host(params)
        self.initialize_models(params)
#        self.initialize_motors(params)
        self.initialize_others(params)
        
        # GPIO pins
#        self.button_gpio = params['button']['gpio']
#        self.led_gpio    = params['led']['gpio']
#        self.pigpio_gpio = params['pigpio']['gpio']
#
#        self.motor_left_forward   = params['motors']['left']['forward_gpio']
#        self.motor_left_backward  = params['motors']['left']['backward_gpio']
#        self.motor_right_forward  = params['motors']['right']['forward_gpio']
#        self.motor_right_backward = params['motors']['right']['backward_gpio']
#
#        self.motor_speed = params['motors']['speed']
        
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
        self.addr = params['host']['addr']
        self.name = params['host']['name']
        self.user = params['host']['user']
        
        if params['host']['test']: 
            log("Testing connection to Raspberry Pi...")
            self.test_connection()
                
    # Initializes App Models according to yml-data
    def initialize_models(self, params):
        if ('buttons') in params:  self.buttons = params['buttons']
#            for button in params['buttons']:
#                self.buttons.append(Button(button['name'], button['color'], button['gpio']))
        else:
            log('No Buttons to be initialized')
#
        if ('leds') in params:  self.leds = params['leds']
#            for led in params['leds']:
#                self.leds.append(LED(led['color'], led['gpio']))
        else:
            log('No LEDs to be initialized')
#
        if ('motors') in params:    self.motors = params['motors']
#            for motor in params['motors']:
#                self.motors.append(Motor(motor['kind'], motor['forward_gpio'],
#                                         motor['backward_gpio'], motor['speed']))
        else:
            log('No Motors to be initialized')
            
    # Initializes Motors
#    def initialize_motors(self, params):
#        if ('motors') in params:
#            for motor in params[motors]:
#               self.motors.append(Button(motor['kind'], motor['forward_gpio'],
#                                         motor['backward_gpio'], motor['speed'])) 
#        else:
#            log('No Motors to be initialized')

    # Initializes Other config parameters
    def initialize_others(self, params):
        self.debug = params['debug']
        self.demo  = params['demo']
        
    # Verifies connection with Raspberry Pi
    def test_connection(self):
        response  = os.system("ping -c 1 " + self.addr)
        if response == 0:
            log('Connection is OK')
        else:
            sys.exit('Connection failed')
