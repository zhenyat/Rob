#!/usr/bin/env python3
################################################################################
#   02_pigpio_receiver_output.py
#
#   <Executable Module Purpose>
#
#   29.06.2019  Created by:  zhenya
################################################################################
from   datetime import datetime
import pigpio

host_addr = '192.168.2.44'
gpio_pin    = 21
ONES_LIMIT  = 10000 # 10000 is arbitrary, adjust as necessary

pi = pigpio.pi(host_addr)

value = pi.read(gpio_pin)
print("===== Initial IR Receiver Output: ", value)    # Initial state is 5V for HX1838

while True:
	while value:                    # Loop until we read '0': signal has come
		value = pi.read(gpio_pin)

	pulse_start = datetime.now()  # Initiate start time of the Data Word

	data_word     = []    # Data Word buffer
	total_ones    = 0
	previos_value = 0     # Used to keep track of transitions from 1 to 0

	while True:
        
		if value != previos_value:
			# The value has changed, so calculate the length of this run
			pulse_end      = datetime.now()
			pulse_duration = pulse_end - pulse_start
			pulse_start    = pulse_end

			data_word.append((previos_value, pulse_duration.microseconds))

		if value:
			total_ones = total_ones + 1
		else:
			total_ones = 0

		if total_ones > ONES_LIMIT:
			break

		previos_value = value
		value = pi.read(gpio_pin)

	print("----------Start----------")
	for (val, pulse) in data_word:
		print('bit: ', val, ' duration (mks): ', pulse)
	print("-----------End-----------\n")

	print(" ===== Size of array is " + str(len(data_word)))
