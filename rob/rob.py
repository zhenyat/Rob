#!/usr/bin/env python3
################################################################################
#   rob.py
#
#   Main App Module

#
#   22.06.2019  Created by: zhenya
################################################################################
from application  import *
from lib.tools    import *

if __name__ == "__main__":
    log("App is starting")
        
    app = Application()

    app.root.mainloop()
  
    log("App is over")