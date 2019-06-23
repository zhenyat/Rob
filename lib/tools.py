################################################################################
#   tools.py
#
#   <Module Purpose>
#
#   22.06.2019  Created by: zhenya
################################################################################
from   pprint import pprint
from   sys    import exit
import time

def debug(object):
    pprint(vars(object))
    
# Timestamp message
def log(message):
    print(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())), message)

def quit():
    log("Completed")
    exit(0)