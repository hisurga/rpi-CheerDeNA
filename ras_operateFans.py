#import wiringpi

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
    print("test")
