#import wiringpi

def initPins():
    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
    io.pinMode(18, io.OUTPUT) 
    return io

def operateFans(io, onoff):
    if onoff == 1:
        io.digitalWrite(18, io.HIGH)
    else:
        io.digitalWrite(18, io.LOW)
    
if __name__ == "__main__":
    print("test")
