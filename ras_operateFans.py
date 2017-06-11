import wiringpi
from time import sleep

def initPin():
    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
    io.pinMode(18, io.OUTPUT) 
    return io

def operateFan(io, onoff):
    if onoff == 1:
        io.digitalWrite(18, io.HIGH)
    else:
        io.digitalWrite(18, io.LOW)
    
if __name__ == "__main__":
    io = initPin()
    while True:
        operateFan(io, 1)
        sleep(10)
        operateFan(io, 0)
        sleep(10)
