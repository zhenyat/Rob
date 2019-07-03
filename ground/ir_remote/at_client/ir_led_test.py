#!/usr/bin/env python3
################################################################################
#   ir_led_test.py
#
#   First test of IR Remote with LED with PIGGPI
#
#   30.06.2019  Created by:  zhenya
################################################################################
import pigpio
import time

host_addr = '192.168.2.44'
gpio_pin  = 21
LED_pin   = 27	
count   = 0

pi = pigpio.pi(host_addr)

while True:
    
    tr = pi.event_trigger(21)
    print(tr)
    time.sleep(1)
    
#if pi.wait_for_event(gpio_pin, 10):
#   print("event detected")
#else:
#   print("wait for event timed out")
   
#while True:
#    try:
#        eve = pi.event_callback(gpio_pin)
#        print(eve.tally())
#        time.sleep(1)
#    except KeyboardInterrupt:
#    #    ...
#        print("Exit by Ctrl+C") 
