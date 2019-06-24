################################################################################
#   tools.py
#
#   <Module Purpose>
#
#   22.06.2019  Created by: zhenya
################################################################################
from   pprint  import pprint
from   sys     import exit
import time
from   tkinter import END

def debug(object):
    pprint(vars(object))
    
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
