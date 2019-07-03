#!/usr/bin/env python3
################################################################################
#   05_gpio_pin_modes.py
#
#
#  Usage of GPIO.gpio_function() to define pin's mode
#
#  http://codius.ru/articles/Raspberry_Pi_3_GPIO_часть_2
#
#   02.07.2019  Created by:  zhenya
################################################################################
import RPi.GPIO as GPIO                 # Импортируем библиотеку по работе с GPIO
import time                             # Импортируем класс для работы со временем
import sys, traceback                   # Импортируем библиотеки для обработки исключений

try:    # Инициализация пинов
    GPIO.setmode(GPIO.BCM)
    pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

    # Для простоты восприятия создадим словарь с возможными значениями
    pin_modes = {0:"GPIO.OUT",
                  1:"GPIO.IN",
                  40:"GPIO.SERIAL",
                  41:"GPIO.SPI",
                  42:"GPIO.I2C",
                  43:"GPIO.HARD_PWM",
                  -1:"GPIO.UNKNOWN"}

    for pin in pins:
        state = GPIO.gpio_function(pin)
        print ("%s %d status: %s" % ("GPIO pin", pin, pin_modes[state]))

    print ("Change pins mode")
    GPIO.setup([2,3,4], GPIO.OUT)
    for pin in [2,3,4]:
        state = GPIO.gpio_function(pin)
        print ("%s %d status: %s" % ("pin", pin, pin_modes[state]))

except KeyboardInterrupt:
    # ...
    print("Exit pressed Ctrl+C")                # Выход из программы по нажатию Ctrl+C
except:
    # ...
    print("Other Exception")                    # Прочие исключения
    print("--- Start Exception Data:")
    traceback.print_exc(limit=2, file=sys.stdout) # Подробности исключения через traceback
    print("--- End Exception Data:")
finally:
    print("CleanUp")                            # Информируем сбросе пинов
    GPIO.cleanup()                              # Возвращаем пины в исходное состояние
    print("End of program")                     # Информируем о завершении работы программы
