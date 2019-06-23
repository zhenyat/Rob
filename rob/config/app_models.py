################################################################################
#   app_models.py
#
#   Generates App Modles and adds them to Dictionary
#
#   23.06.2019  Created by: zhenya
################################################################################
import gpiozero as GPIO
from lib.tools import debug

class AppModels():
  def __init__(self, config):
    
    if config.demo:
        self.button = GPIO.Button(config.button_gpio, pin_factory=config.factory)
        self.led    = GPIO.LED(config.led_gpio, pin_factory=config.factory)

        self.motor_left  = GPIO.Motor(forward=config.motor_left_forward,  backward=config.motor_left_backward,  pin_factory=config.factory)
        self.motor_right = GPIO.Motor(forward=config.motor_right_forward, backward=config.motor_right_backward, pin_factory=config.factory)
        
    else:
        self.robot = GPIO.Robot(left=(config.motor_left_forward,    config.motor_left_backward),
                           right=(config.motor_right_forward, config.motor_right_backward), pin_factory=config.factory)
        