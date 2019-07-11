################################################################################
#   application.py
#
#   This module initializes the App
#
#   22.06.2019  Created by: zhenya
################################################################################
from config.app_config import *
from config.app_models import *
from views.demo        import *
from views.robot       import *
from   lib.tools            import *


class Application:
    def __init__(self):
        self.models = []
        config = AppConfig()
        if (debug): debug(config)
        
        models = AppModels(config)

        self.root = Tk()
        
        if config.demo:
            DemoView(self.root, config, models)
        else:
            RobotView(self.root, config, models)
            