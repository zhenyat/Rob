################################################################################
#   tools.py
#
#   Pool of Functions for App
#
#   22.06.2019  Created by: zhenya
#   20.07.2019  Functions get_logo() & get_gif_logo() added
################################################################################
from   pprint  import pprint
from   sys     import exit
import time
from   tkinter import END, PhotoImage
from   PIL     import Image, ImageTk 

def debug(object):
    pprint(vars(object))

# Gets log as non-GIF file
def get_logo(file, size):
    img = Image.open(file)
    img = img.resize((size, size), Image.ANTIALIAS)
    
    return ImageTk.PhotoImage(img)

# Gets log as GIF file
def get_gif_logo(file, factor):
    logo = PhotoImage(file=file)
    return logo.subsample(factor)
    
    
# Timestamp message
def log(message):
    print(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())), message)

def quit():
    log("Completed")
    exit(0)

#################################################
#   Reports to the output widget
#################################################
def report(out_box, text, reset=False):
    if reset: out_box.delete(1.0, END)
    
    out_box.insert(END, text + '\n')
    out_box.update()
