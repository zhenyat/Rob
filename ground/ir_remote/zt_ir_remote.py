#!/usr/bin/env python3
################################################################################
#   zt_ir_remote.py
#
#   No LIRC approach
#
#   Ref:  https://apps.fishandwhistle.net/archives/1115
#
#   01.07.2019  Created by: zhenya
################################################################################
import RPi.GPIO as GPIO
from   time import time

class IRControl():
    def __init__(self, pin, logical_pinout=True, pull_up=True):
        self.pin = pin

        if logical_pinout: GPIO.setmode(GPIO.BCM)      # Logical  pinout
        else:              GPIO.setmode(GPIO.BOARD)    # Physical pinout

        if pull_up:
            GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.action)
        else:
            GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.action)
           
        print('initial')

    # Call-back function
    def action():
        code = str(hex(read_code()))
        print("Event: ", code)
    
    # Gets data from a pin as an array of bits for the period 'duration' in sec
    def get_bits(self, duration):
        start_time = time()
        bits       = []
        while (time() - start_time) < duration:
            bits.append(GPIO.input(self.pin))

        return bits

    # Identifies the code of Receiver output signal. Reading time is in ms
    def read_code(self, reading_time=150):
        bits         = get_bits(reading_time/1000.0)
        array_length = len(bits)
        
        if array_length < reading_time:
            return None

        rate = array_length / (reading_time / 1000.0) # acquisition rate (per s)

        pulses   = []
        i_break  = 0

        # Detect run lengths using the acquisition rate to turn the times into microseconds
        for i in range(1, array_length):
            if (bits[i] != bits[i-1]) or (i == array_length-1):
                pulses.append((bits[i-1], int((i-i_break)/rate*1e6)))
                i_break = i

        # Decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
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
        except ValueError:          # probably an empty code
            return None

    def destroy(self):
        GPIO.cleanup()

#  def wait_signal(self):
#    while True:
#        print("Waiting for signal")
#        if (self.pull_up):
#            edge_detect = GPIO.wait_for_edge(self.pin, GPIO.FALLING)
#        else:
#            edge_detect = GPIO.wait_for_edge(self.pin, GPIO.RISING)
# 
#        if edge_detect:
#            return(str(hex(read_code())))
