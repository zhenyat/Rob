################################################################################
#   app_config.py
#
#   App configuration:
#       - reads input data
#       - tests connection to Raspberry Pi
#
#   22.06.2019  Created by: zhenya
#   10.07.2019  New data structure of LEDs, Buttons, etc
#   20.07.2019  Models & Code cleaning
################################################################################
import os
import sys
import yaml

from controllers.gpio import *
from lib.tools        import *

class AppConfig():
    
    def __init__(self):
        
        params = self.read_values()

        self.initialize_host(params)
        self.initialize_models(params)
        self.initialize_others(params)
                
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
        if ('buttons') in params: self.buttons = params['buttons']
        else:                     log('No Buttons to be initialized')
#
        if ('leds') in params: self.leds = params['leds']
        else:                  log('No LEDs to be initialized')
#
        if ('motors') in params: self.motors = params['motors']
        else:                    log('No Motors to be initialized')
            
    # Initializes Other config parameters
    def initialize_others(self, params):
        self.debug = params['debug']
        self.demo  = params['demo']
        
    # Verifies connection with Raspberry Pi
    def test_connection(self):
        response  = os.system("ping -c 1 " + self.addr)
        if response == 0: log('Connection is OK')
        else:             sys.exit('Connection failed')
