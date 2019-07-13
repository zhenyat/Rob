################################################################################
#   gpio.py
#
#   GPIO Demo / Tests Controller
#
#   22.06.2019  Created by: zhenya
#   13.07.2019  Updated for Models
################################################################################
from   time      import sleep
import pigpio

from   lib.tools import *

def button(buttons, out_box):
    report(out_box, '===== Buttons Demo', True)
    
    for button in buttons:
        report(out_box, "  Button '%s' (%s)" % (button.name, button.color))
        for i in range(5):
            if button.button_gpio.is_pressed:
                report(out_box, "    %i: Button is ON" %i)
                sleep(1)
            else:
                report(out_box, "    %i: Button is OFF" %i)
                sleep(1)

    report(out_box, "===== End Demo")

def leds_blink(leds, out_box):
    report(out_box, '===== LEDs Blinking', True)

    for led in leds:
        report(out_box, "  LED '%s'" % led.color)
        report(out_box, "  blinking...")
        led.blink(2)
        
        for i in range(2):
            report(out_box, "    LED is ON")
            led.on()
            sleep(0.5)
            report(out_box, "    LED is OFF")
            led.off()
            sleep(0.5)

    report(out_box, "===== End Demo")

def led_by_button(button, led, out_box):
    report(out_box, '===== LED by button', True)
    report(out_box, " press %s button" % button.color)
    
    for i in range(6):
        if button.is_pressed():
            led.on()
            report(out_box, "    %s LED is ON" % led.color)
            sleep(1)
        else:
            led.off()
            report(out_box, "    %s LED is OFF" % led.color)
            sleep(1)

    led.off()
    report(out_box, "===== End Demo")

def motors(motor_left, motor_right, speed, out_box):
    report(out_box, '===== Motors Demo', True)

    report(out_box, '    Left motor forward')
    motor_left.forward(speed)
    sleep(2)

    report(out_box, '    Left motor backward')
    motor_left.backward(speed)
    sleep(2)

    report(out_box, '    Left motor stop')
    motor_left.stop()

    report(out_box, '    Right motor forward')
    motor_right.forward(speed)
    sleep(2)

    report(out_box, '    Right motor backward')
    motor_right.backward(speed)
    sleep(2)

    report(out_box, '    Right motor stop')
    motor_right.stop()

    report(out_box, "===== End Demo")

#################################################
#   Toggles voltage on a given GPIO pin
#   For better demo-effect the LED pin to be used
#################################################
def pigpio_toggle(host_addr, gpio_pin, out_box):
    report(out_box, '===== pigpio Lib Demo', True)

    pi = pigpio.pi(host_addr)

    for i in range(4):
        if pi.read(gpio_pin) == 0:
            pi.write(gpio_pin, 1)
        else:
            pi.write(gpio_pin, 0)

        report(out_box, '   On pin: %d' % pi.read(gpio_pin))
        sleep(2)

    report(out_box, "===== End Demo")
