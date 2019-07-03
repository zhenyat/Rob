################################################################################
#   RPi_template.py
#
#   Template fro RPi.GPIO 
#
#   http://codius.ru/articles/Raspberry_Pi_3_GPIO_введение
#
#   28.06.2019  Created by: zhenya
################################################################################

import RPi.GPIO as GPIO

print("===== Start of program")
try:
    pass
    # === Инициализация пинов ===
    #pin=5                                
    #GPIO.setmode(GPIO.BCM)                 
    #GPIO.setup(pin, GPIO.OUT, initial=1)   

    # Здесь размещаем основной рабочий код
    # ...

except KeyboardInterrupt:
    # ...
    print("Exit by Ctrl+C") 
except:
    # ...
    print("Other Exceptions") 
finally:
    GPIO.cleanup()          
    print("===== End of program")