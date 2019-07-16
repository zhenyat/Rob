################################################################################
#   app_models.py
#
#   Generates Models
#
#   23.06.2019  Created by: zhenya
#   13.07.2017  Update for Models
################################################################################
from  models.button import *
from  models.host   import *
from  models.led    import *
from  models.motor  import *
from  models.robot  import *

class AppModels():
    def __init__(self, config):
        
        self.host = Host(config.addr, config.name, config.user)

        if (config.buttons):
            self.buttons = []
            for button in config.buttons:
                self.buttons.append(Button(button['name'], button['color'], button['gpio'], self.host.factory))

        if (config.leds):
            self.leds    = []
            for led in config.leds:
                self.leds.append(LED(led['color'], led['gpio'], self.host.factory))

            self.colorize_leds()
            
        if (config.demo):
            if (config.motors):
                motors  = []
                for motor in config.motors:
                    motors.append(Motor(motor['side'], motor['forward_gpio'],
                                             motor['backward_gpio'], motor['speed'], self.host.factory))
                self.nominate_motors(motors)
        else:
            self.robot = Robot(config.motors, self.host.factory)

    def colorize_leds(self):
        for led in self.leds:
            if   led.color == 'red':    self.led_red    = led
            elif led.color == 'green':  self.led_green  = led
            elif led.color == 'blue':   self.led_blue   = led
            elif led.color == 'yellow': self.led_yellow = led
            elif led.color == 'white':  self.led_white  = led

    def nominate_motors(self, motors):
        for motor in motors:
            if motor.side == 'left':
                self.motor_left  = motor.motor_gpio
            else:
                self.motor_right = motor.motor_gpio
        self.motor_speed = motors[0].speed
