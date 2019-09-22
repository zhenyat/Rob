################################################################################
#   demo.py
#
#   Demo View
#
#   23.06.2019  Created by: zhenya
#   12.07.2019  Updated for Models
#   20.07.2019  Updated for logo (mainloop() must be here!)
################################################################################
from tkinter import *

import controllers.gpio as gpio
from lib.tools          import *

class DemoView():
    def __init__(self, master, models):
        self.master = master
        
        # Default attribures
        self.master.title('Raspberry Pi Robot: ' + models.host.addr)
        self.master.geometry(self.center())
        self.master.attributes("-topmost", True)         # Place master over all other windows
        self.master.config(background = 'lightyellow')
        self.master.resizable(False, False)

        ######  Widgets
        
        ###     GPIO Demo
        demo_frame = LabelFrame(master, text='GPIO Demo', width=400, height=50, background='lightblue', bd=2, labelanchor=N)
        demo_frame.grid(row=0, column=0)

        # Logo
        logo = get_logo('images/logo.png', size=25)
#       logo = get_gif_logo('images/logo.gif', factor=10)
        Label(demo_frame, image=logo).grid(row=0, column=0, sticky=N)
        
        # Button Ex.
        button_buttons = Button(demo_frame, text='Buttons', highlightbackground ="blue", command=lambda: gpio.button(models.buttons, log_box))
        button_buttons.grid(row=0, column=1, columnspan = 4, sticky=W)

        # LED Ex.
        button_led = Button(demo_frame, text='LEDs', highlightbackground ="blue", command=lambda: gpio.leds_blink(models.leds, log_box))
        button_led.grid(row=0, column=5,  columnspan = 3, sticky=N)

        # Button for LED Ex.
        button_for_led = Button(demo_frame, text='Button & LED', highlightbackground ="blue", command=lambda: gpio.led_by_button(models.buttons[0], models.led_yellow, log_box))
        button_for_led.grid(row=0, column=8, columnspan = 5, sticky=W)

        # pigpio Ex.
        button_pigpio = Button(demo_frame, text='pigpio', highlightbackground ="blue", command=lambda: gpio.pigpio_toggle(models.host.addr, models.led_yellow.pin._number, log_box))
        button_pigpio.grid(row=0, column=13,  columnspan = 3, sticky=N)

        # Motors Ex.
        button_motors = Button(demo_frame, text='Motors', highlightbackground ="blue", command=lambda: gpio.motors(models.motor_left, models.motor_right, models.motor_speed, log_box))
        button_motors.grid(row=0, column=16,  columnspan = 3, sticky=N)

        log_box = Text(demo_frame, width = 60, height = 20, bg = 'lightblue')
        log_box.grid(row = 1, column = 0, columnspan =20, sticky = N)

        ###     Bottom
        self.bottom_frame = Frame(master, width=300, background='light cyan')
        self.bottom_frame.grid(row=2, sticky=W)

        self.quit_button  = Button(self.bottom_frame, text="Quit", highlightbackground ="grey", command=quit)
        self.quit_button.grid(row=0, column=0)

        self.master.mainloop()
        
    # Locates GUI (View) window in the center of a screen
    def center(self):
        masterWidth  = 800
        masterHeight = 600

        screenWidth  = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()

        masterX = (screenWidth  - masterWidth)  / 2
        masterY = (screenHeight - masterHeight) / 2

        return('%dx%d+%d+%d' % (masterWidth, masterHeight, masterX, masterY))
