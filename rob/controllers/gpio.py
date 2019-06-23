################################################################################
#   gpio.py
#
#   GPIO Demo / Tests Controller
#
#   22.06.2019  Created by: zhenya
################################################################################
from   time    import sleep
from   tkinter import END
import pigpio

def button(button, out_box):
    out_box.delete(1.0, END)
    report(out_box, '===== Button Demo')
    
    for i in range(10):
        if button.is_pressed:
            report(out_box, "    %i: Button is ON" %i)
            sleep(1)
        else:
            report(out_box, "    %i: Button is OFF" %i)
            sleep(1)

    report(out_box, "===== End Demo")

def led_blink(led, out_box):
    out_box.delete(1.0, END)
    report(out_box, '===== LED Blinking')

    for i in range(4):
        report(out_box, "    LED is ON")
        led.on()
        sleep(0.5)
        report(out_box, "    LED is OFF")
        led.off()
        sleep(0.5)

    report(out_box, "===== End Demo")

def led_by_button(button, led, out_box):
    out_box.delete(1.0, END)
    report(out_box, '===== LED by button')

    for i in range(6):
        if button.is_pressed:
            led.on()
            report(out_box, "    LED is ON")
            sleep(1)
        else:
            led.off()
            report(out_box, "    LED is OFF")
            sleep(1)

    led.off()
    report(out_box, "===== End Demo")

def motors(motor_left, motor_right, speed, out_box):
    out_box.delete(1.0, END)
    report(out_box, '===== Motors Demo')

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
    out_box.delete(1.0, END)
    report(out_box, '===== pigpio Lib Demo')

    pi = pigpio.pi(host_addr)

    for i in range(4):
        if pi.read(gpio_pin) == 0:
            pi.write(gpio_pin, 1)
        else:
            pi.write(gpio_pin, 0)

        report(out_box, '   On pin: %d' % pi.read(gpio_pin))
        sleep(2)

    report(out_box, "===== End Demo")

#################################################
#   Reports to the output widget
#################################################
def report(out_box, text):
    out_box.insert(END, text + '\n')
    out_box.update()

