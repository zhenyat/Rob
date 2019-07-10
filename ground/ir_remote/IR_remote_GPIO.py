import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import time

#Define the GPIO
INPUT_WIRE = 18
LED1=12
LED2=16
LED3=20
LED4=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_WIRE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)

#toggle the LED's
def ledonoff(person):
    if GPIO.input(person)==0:
	GPIO.output(person,True)
	sleep(.5)
    else:
	GPIO.output(person,False)
	sleep(.5)

print ""
print "IR remote switch"
print "----------------"

while True:
	#first section of code is to detect the start bit
	high_previous = False
	while True:
  	  if not high_previous:
	   while GPIO.input(INPUT_WIRE):pass
	   pulse_high = datetime.now()
	  while not GPIO.input(INPUT_WIRE):pass
	  pulse_low = datetime.now()
	  pulseLength = pulse_low - pulse_high
	  while GPIO.input(INPUT_WIRE):pass
	  pulse_high = datetime.now()
	  off_time = pulse_high - pulse_low
	  high_previous = True
	  if pulseLength.microseconds > 3000 :
		if pulseLength.microseconds > 6000 : start_big = True
		else : start_big = False
		if off_time.microseconds < 3000 : repeat_code = True
		else : repeat_code = False
		break

	#this part of the program reads the address byte and command 
	#byte providing it hasn't recived the repeate code
	command = []
	if not repeat_code :
	  while True:
		while not GPIO.input(INPUT_WIRE):pass
		pulse_low = datetime.now()
		while GPIO.input(INPUT_WIRE):pass
		pulse_high = datetime.now()
		off_time = pulse_high - pulse_low
		if off_time.microseconds > 2500 : break
		if off_time.microseconds < 1000 : command.append(0)
		else : command.append(1)

	#this part of the program prints to the screen the results
#	if len(command) < 2 : print "REPEAT"
	if len(command) < 2 : print ""
	elif len(command) == 32 :
	  bit = 0b10000000
	  address = 0
	  address_inv = 0
	  instruction = 0
	  instruction_inv = 0
	  for position in range(8) :
		if command[position] : 	address = address | bit
		if command[position +8] : address_inv = address_inv | bit
		if command[position +16] : instruction = instruction | bit
		if command[position +24] : instruction_inv = instruction_inv | bit
		bit = bit >> 1
#Snif the remote 
	  print "Big start bit = " + str(start_big)
	  print "Byte 1 = " + str(address)
	  print "Byte 2 = " + str(address_inv)
	  print "Byte 3 = " + str(instruction)
	  print "Byte 4 = " + str(instruction_inv) 

# Codetabel voor VANTAGE X2-YC01N afstandsbediening
# Print key
	  if instruction == 48 and instruction_inv == 207 :
		print "Power"
		ledonoff(int('20'))
	  if instruction == 170 and instruction_inv == 85 :
		print "Mute"
		ledonoff(int('21'))
	  if instruction == 144 and instruction_inv == 111 :
		print "1"
		ledonoff(int('16'))
	  if instruction == 160 and instruction_inv == 95 :
		print "2"
	  if instruction == 128 and instruction_inv == 127 :
		print "3"
	  if instruction == 210 and instruction_inv == 45 :
		print "4"
	  if instruction == 226 and instruction_inv == 29 :
		print "5"
	  if instruction == 194 and instruction_inv == 61 :
		print "6"
	  if instruction == 82 and instruction_inv == 173 :
		print "7"
	  if instruction == 98 and instruction_inv == 157 :
		print "8"
	  if instruction == 66 and instruction_inv == 189 :
		print "9"
	  if instruction == 130 and instruction_inv == 125 :
		print "0"
	  if instruction == 88 and instruction_inv == 167 :
		print "multimedia"
	  if instruction == 154 and instruction_inv == 101 :
		print "Last"
	  if instruction == 56 and instruction_inv == 199 :
		print "MoSAic"
	  if instruction == 24 and instruction_inv == 231 :
		print "Sleep"
	  if instruction == 40 and instruction_inv == 215 :
		print "Audio"
	  if instruction == 8 and instruction_inv == 247 :
		print "INFO"
	  if instruction == 34 and instruction_inv == 221 :
		print "up"
	  if instruction == 18 and instruction_inv == 237 :
		print "down"
	  if instruction == 80 and instruction_inv == 175 :
		print "OK"
		ledonoff(int('12'))
	  if instruction == 50 and instruction_inv == 205 :
		print "left"
	  if instruction == 2 and instruction_inv == 253 :
		print "right"
	  if instruction == 192 and instruction_inv == 63 :
		print "Menu"
	  if instruction == 186 and instruction_inv == 69 :
		print "EPG"
	  if instruction == 96 and instruction_inv == 159 :
		print "SAT"
	  if instruction == 146 and instruction_inv == 109 :
		print "Back"
	  if instruction == 176 and instruction_inv == 79 :
		print "Vol+"
	  if instruction == 208 and instruction_inv == 47 :
		print "Vol-"
	  if instruction == 218 and instruction_inv == 37 :
		print "Page up"
	  if instruction == 234 and instruction_inv == 21 :
		print "Page down"
	  if instruction == 64 and instruction_inv == 191 :
		print "PR+"
	  if instruction == 120 and instruction_inv == 135 :
		print "PR-"
	  if instruction == 162 and instruction_inv == 93 :
		print "Text"
	  if instruction == 10 and instruction_inv == 245 :
		print "Zoom"
	  if instruction == 58 and instruction_inv == 197 :
		print "FAV"
	  if instruction == 240 and instruction_inv == 15 :
		print "F0"
	  if instruction == 112 and instruction_inv == 143 :
		print "F1"
	  if instruction == 0 and instruction_inv == 255 :
		print "F2"
GPIO.cleanup() 
