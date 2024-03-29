#!/usr/bin/env python3

#   Curses Test with Robot

import curses 
import gpiozero             as GPIO
from   gpiozero.pins.pigpio import PiGPIOFactory
from   time                 import sleep

addr = '192.168.2.44'
factory = PiGPIOFactory(host=addr)
GPIO.Device.pin_factory = factory         # Workaround: MUST BE!!!

robot = GPIO.Robot(left=(19, 16), right=(22, 23), pin_factory=factory)
speed = 1

# Init curses and set it up
screen = curses.initscr()
curses.noecho()             # no echoing of keys to the screen
curses.cbreak()             # to react on a key instantly without Enter (buffering)
screen.keypad(True)         # enable keypad mode (can return curses.KEY_UP, etc.)

try:
    while True:
        char = screen.getch()
        
        if char == ord('q'):
            print('\r\rQuit')
            sleep(2)
            break
        elif char == curses.KEY_UP:
            print('\rFORWARD')
            robot.forward(speed)
        elif char == curses.KEY_DOWN:
            print('\rBACKWORD')
            robot.backward(speed)
        elif char == curses.KEY_RIGHT:
            print('\rRIGHT')
            robot.right(speed)
        elif char == curses.KEY_LEFT:
            print('\rLEFT')
            robot.left(speed)
        else: 
            pass

finally:
    robot.stop()
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()
    