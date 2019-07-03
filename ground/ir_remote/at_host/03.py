#!/usr/bin/env python3
################################################################################
#   03_get_codes.py
#
#  Gathers codes of Receiver output signals 
#
#   # Ref:  https://apps.fishandwhistle.net/archives/1115
#
#   30.06.2019  Created by:  zhenya
################################################################################
import RPi.GPIO as     GPIO
from   time     import time
import sys

ir_pin = 40
def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(ir_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()    # seconds
    results = []
    k = 0
    ones = 0
    zeroes = 0
    while (time() - t0) < duration:
        signal = GPIO.input(pin)
        if (k < 8): print(k, ' - ', signal)
        results.append(signal)
        print(k, results)
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None

def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        print("Starting IR Listener")
        while True:
            print("Waiting for signal")
            edge_detect = GPIO.wait_for_edge(ir_pin, GPIO.FALLING)
            if edge_detect:
                res = binary_aquire(ir_pin, 0.15)
                print("---- res: ", res)
#            code = on_ir_receive(ir_pin)
#            if code:
#                print(str(hex(code)), ' - ', code)
#                if(hex(code) == '0xff18e7'): print('==== UP! ===')
#            else:
#                print("Invalid code")
    except KeyboardInterrupt:
        print('Ctrl C')
        sys.exit('Connection failed')
    except RuntimeError:
        # this gets thrown when control C gets pressed
        # because wait_for_edge doesn't properly pass this on
        pass
    print("Quitting")
    destroy()
