################################################################################
#   application.py
#
#   This module initializes the App
#
#   22.06.2019  Created by: zhenya
#   13.07.2019  Last update
################################################################################
from config.app_config  import *
from config.app_models  import *
from views.demo         import *
from views.motion       import *

class Application:
    def __init__(self):
        self.models = []
        config = AppConfig()
        models = AppModels(config)

        self.root = Tk()

        if config.demo:
            DemoView(self.root, models)
        else:
            MotionView(self.root, models)
