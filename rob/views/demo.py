################################################################################
#   demo.py
#
#   Demo View
#
#   23.06.2019  Created by: zhenya
################################################################################
from tkinter import *

import controllers.gpio  as gpio

class DemoView():
    def __init__(self, master, config, models):
        self.master = master
        self.config = config
        
        # Default attribures
        self.master.title('Raspberry Pi Robot: ' + config.host_addr)
        self.master.geometry(self.center())
        self.master.attributes("-topmost", True)         # Place master over all other windows
        self.master.config(background = 'lightyellow')
        self.master.resizable(False, False)

        ######  Widgets
        
        ###     GPIO Demo
        demo_frame = LabelFrame(master, text='GPIO Demo', width=400, height=50, background='lightblue', bd=2, labelanchor=N)
        demo_frame.grid(row=0)
        
        # Button Ex.
        button_button = Button(demo_frame, text='Button', highlightbackground ="blue", command=lambda: gpio.button(models.button, log_box))
        button_button.grid(row=0, column=1, columnspan = 3, sticky=W)

        # LED Ex.
        button_led = Button(demo_frame, text='LED', highlightbackground ="blue", command=lambda: gpio.led_blink(models.led, log_box))
        button_led.grid(row=0, column=4,  columnspan = 3, sticky=N)

        # Button for LED Ex.
        button_for_led = Button(demo_frame, text='Button & LED', highlightbackground ="blue", command=lambda: gpio.led_by_button(models.button, models.led, log_box))
        button_for_led.grid(row=0, column=7, columnspan = 5, sticky=W)

        # pigpio Ex.
        button_pigpio = Button(demo_frame, text='pigpio', highlightbackground ="blue", command=lambda: gpio.pigpio_toggle(config.host_addr, config.led_gpio, log_box))
        button_pigpio.grid(row=0, column=12,  columnspan = 3, sticky=N)

        # Motors Ex.
        button_motors = Button(demo_frame, text='Motors', highlightbackground ="blue", command=lambda: gpio.motors(models.motor_left, models.motor_right, config.motor_speed, log_box))
        button_motors.grid(row=0, column=15,  columnspan = 3, sticky=N)

        log_box = Text(demo_frame, width = 60, height = 20, bg = 'lightblue')
        log_box.grid(row = 1, column = 0, columnspan =19, sticky = N)
        
        ###     Bottom
        self.bottom_frame = Frame(master, width=300, background='light cyan')
        self.bottom_frame.grid(row=2, sticky=W)

        self.quit_button  = Button(self.bottom_frame, text="Quit", highlightbackground ="grey", command=quit)
        self.quit_button.grid(row=0, column=0)

    # Locates GUI (View) window in the center of a screen
    def center(self):
        masterWidth  = 800
        masterHeight = 600

        screenWidth  = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()

        masterX = (screenWidth  - masterWidth)  / 2
        masterY = (screenHeight - masterHeight) / 2

        return('%dx%d+%d+%d' % (masterWidth, masterHeight, masterX, masterY))