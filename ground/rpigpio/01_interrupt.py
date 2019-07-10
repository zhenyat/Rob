#!/usr/bin/env python3
################################################################################
#   01_interrupt.py
#
#   RPi.GPIO Interruption with Button
#
#   03.07.2019  Created by:  zhenya
################################################################################
import time
import RPi.GPIO as GPIO

# handle the button event
def buttonEventHandler():
    print("handling button event")

    for i in range(2):
        GPIO.output(27,True)    # turn the LED on
        time.sleep(1)
        GPIO.output(27,False)   # turn the LED off

# main function
def main():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(27, GPIO.OUT)
    
    GPIO.add_event_detect(17,GPIO.FALLING)
    GPIO.add_event_callback(17,buttonEventHandler)

    # make the red LED flash
    while True:
        GPIO.output(27,True)
        time.sleep(0.5)
        GPIO.output(27,False)
        time.sleep(0.5)

    GPIO.cleanup()

main()