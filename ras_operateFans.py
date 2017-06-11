import wiringpi2
from time import sleep

FANPIN = 18

def initPin():
    wiringpi2.wiringPiSetupGpio()
    wiringpi2.pinMode(FANPIN, 1)
    
def operateFan(onoff):
    if onoff == 1:
        wiringpi2.digitalWrite(FANPIN, 1)
    else:
        wiringpi2.digitalWrite(FANPIN, 0)
    
if __name__ == "__main__":
    initPin()
    while True:
        operateFan(1)
        sleep(1)
        operateFan(0)
        sleep(1)
