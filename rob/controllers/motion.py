################################################################################
#   motion.py
#
#   export TERM=linux
#export TERMINFO=/etc/terminfo
#   Robot motion function
#
#   23.06.2019  Created by: zhenya
#   24.06.2019  Last update
################################################################################
from   time      import sleep
import pigpio

from   lib.tools import *

def keyboard_warning(out_box):
    text = 'Attention! Robot control by keys to be done in CLI only\n\n Run file: bin/motion_by_keys'
    report(out_box, text, True)

def square_motion(robot, speed, out_box):
    report(out_box, '===== Square Motion', True)
    
    pi = pigpio.pi('192.168.2.44')
    
    for i in range(4):
        robot.forward(speed)
        report(out_box, '   On pin: %d | %d' % (pi.read(19), pi.read(16)))
        report(out_box, '      Forward...')
        sleep(1)
        robot.backward(speed)
        report(out_box, '   On pin: %d | %d' % (pi.read(19), pi.read(16)))
        report(out_box, '      Back...')
        sleep(1)

    robot.stop()
    report(out_box, "===== End Motion")
