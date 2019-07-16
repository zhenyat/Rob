################################################################################
#   robot.py
#
#   Robot class
#
#   Arguments:
#       robot_gpio   - GPIO Object
#       motors_speed - Motors speed    
#
#   12.07.2019  Created by:  zhenya
################################################################################
import gpiozero as GPIO

class Robot():
    def __init__(self, motors, factory):

        for motor in motors:
            if motor['side'] == 'left':
                left_forward  = motor['forward_gpio']
                left_backward = motor['backward_gpio']
            else:
                right_forward  = motor['forward_gpio']
                right_backward = motor['backward_gpio']
                 
        self.robot_gpio = GPIO.Robot(left=(left_forward, left_backward),
                                     right=(right_forward, right_backward), 
                                     pin_factory=factory)
        self.motors_speed = motors[0]['speed']

    def backward(self, speed):
        self.robot_gpio.backward(speed)

    def forward(self, speed):
        self.robot_gpio.forward(speed)

    def stop(self):
        self.robot_gpio.stop()
