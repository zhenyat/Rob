#!/usr/bin/env python3
################################################################################
#   02_receiver_output.py
#
#   Identifies IR receiver output (model: HX1838)
#
#   REf:  https://blog.bschwind.com/2016/05/29/sending-infrared-data_words-from-a-raspberry-pi-without-lirc/
#
#   29.06.2019  Created by:  zhenya
################################################################################
import RPi.GPIO as GPIO
from   datetime import datetime

IR_PIN      = 40    # GPIO21
ONES_LIMIT  = 10000 # 10000 is arbitrary, adjust as necessary

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_PIN, GPIO.IN) # To read IR Receiver signals 

value = GPIO.input(IR_PIN)
print("===== Initial IR Receiver Output: ", value)    # Initial state is 5V for HX1838

while True:
	while value:                    # Loop until we read '0': signal has come
		value = GPIO.input(IR_PIN)

	pulse_start = datetime.now()  # Initiate start time of the Data Wordnano 

	data_word = []              # Data Word buffer

	# The end of the "data_word" happens when we read more than
	# a certain number of '1' (1 is off for HX1838 receiver)
	total_ones = 0

	previos_value = 0     # Used to keep track of transitions from 1 to 0

	while True:

		if value != previos_value:
			# The value has changed, so calculate the length of this run
			pulse_end      = datetime.now()
			pulse_duration = pulse_end - pulse_start
			pulse_start    = pulse_end

			data_word.append((previos_value, pulse_duration.microseconds)/1000.0)

		if value:
			total_ones = total_ones + 1
		else:
			total_ones = 0

		if total_ones > ONES_LIMIT:
			break

		previos_value = value
		value = GPIO.input(IR_PIN)

	print("----------Start----------")
	for (val, pulse) in data_word:
		print('bit: ', val, ' duration (mks): ', pulse)
	print("-----------End-----------\n")

	print(" ===== Size of array is " + str(len(data_word)))
