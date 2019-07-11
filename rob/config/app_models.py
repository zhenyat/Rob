################################################################################
#   app_models.py
#
#   Generates GPIO Objects and adds
#
#   23.06.2019  Created by: zhenya
#   10.07.2017
################################################################################
#import gpiozero as GPIO

from   models.button import *
from   models.host          import *
from   models.led           import *
from   models.motor         import *
#from lib.tools import debug

class AppModels():
    def __init__(self, config):
        
        self.host = Host(config.addr, config.name, config.user)
        print(self.host.factory)
        if (config.buttons):
            self.buttons = []
            for button in config.buttons:
                self.buttons.append(Button(button['name'], button['color'], button['gpio'], self.host.factory))

        if (config.leds):
            self.leds    = []
            for led in config.leds:
                self.leds.append(LED(led['color'], led['gpio'], self.host.factory))
 
        if (config.motors):
            self.motors  = []
            for motor in config.motors:
                self.motors.append(Motor(motor['kind'], motor['forward_gpio'],
                                         motor['backward_gpio'], motor['speed']))

        print(self.motors[0].backward_gpio)
#    if config.demo:
#        self.button = GPIO.Button(config.button_gpio, pin_factory=config.factory)
#        self.led    = GPIO.LED(config.led_gpio, pin_factory=config.factory)
#
#        self.motor_left  = GPIO.Motor(forward=config.motor_left_forward,  backward=config.motor_left_backward,  pin_factory=config.factory)
#        self.motor_right = GPIO.Motor(forward=config.motor_right_forward, backward=config.motor_right_backward, pin_factory=config.factory)
#        
#    else:
#        self.robot = GPIO.Robot(left=(config.motor_left_forward,   config.motor_left_backward),
#                                right=(config.motor_right_forward, config.motor_right_backward), pin_factory=config.factory)
