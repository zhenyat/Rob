#!/usr/bin/env python3
################################################################################
#   yml_handling.py
#
#   <Executable Module Purpose>
#
#   10.07.2019  Created by:  zhenya
################################################################################
import os
import sys
import yaml
from   lib.tools import *


with open('./params.yml', 'r') as stream:
    try:
        data = (yaml.safe_load(stream))          # Return Dictionary
        print(len(data['leds']), data['leds'])
        if ('buttons') in data:
            print("YES")
        else:
            print("NO")
    except yaml.YAMLError as error_message:
        log(error_message)
        sys.exit("Failed to read params")
