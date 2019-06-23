################################################################################
#   application.py
#
#   This module initializes the App
#
#   22.06.2019  Created by: zhenya
################################################################################
from tkinter import *

from config.app_config import *
from config.app_models import *
from lib               import *
from views.demo        import *


class Application:
    def __init__(self):
        config = AppConfig()
        models = AppModels(config)

        self.root = Tk()
        AppView(self.root, config, models)