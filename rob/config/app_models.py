################################################################################
#   app_models.py
#
#   Generates Models Objects
#
#   23.06.2019  Created by: zhenya
#   13.07.2017  Update for Models
#   22.09.2019  Corrections done
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
                self.buttons.append(Button(button['gpio'], self.host.factory, button['name'], button['color']))

        if (config.leds):
            self.leds    = []
            for led in config.leds:
                self.leds.append(LED(led['gpio'], self.host.factory, led['color']))

            self.colorize_leds()

        if (config.demo):
            if (config.motors):
                motors  = []
                for motor in config.motors:
                    motors.append(Motor(motor['forward_gpio'], motor['backward_gpio'], 
                                        self.host.factory, motor['side'], motor['speed']))
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
                self.motor_left  = motor
            else:
                self.motor_right = motor
        self.motor_speed = motors[0].speed
