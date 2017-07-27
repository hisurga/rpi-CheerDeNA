#-*- coding: utf-8 -*-
import wiringpi2
from time import sleep

FANPIN = 18

wiringpi2.wiringPiSetupGpio()
wiringpi2.pinMode(FANPIN, 1)

while True:
    print("ON")
    wiringpi2.digitalWrite(FANPIN, 1)
    sleep(5)

    print("OFF")
    wiringpi2.digitalWrite(FANPIN, 0)
    sleep(5)
