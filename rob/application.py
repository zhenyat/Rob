################################################################################
#   application.py
#
#   This module initializes the App
#
#   22.06.2019  Created by: zhenya
################################################################################
from config.app_config  import *
from config.app_models  import *
from views.demo         import *
from views.robot        import *
from lib.tools          import *

class Application:
    def __init__(self):
        self.models = []
        config = AppConfig()
#        if (debug): debug(config)
        
        models = AppModels(config)
#        debug(models)
        print(models.host.addr)
#        
#        self.root = Tk()
#        
#        if config.demo:
#            DemoView(self.root,  config, gpio_objects)
#        else:
#            RobotView(self.root, config, gpio_objects)
#            