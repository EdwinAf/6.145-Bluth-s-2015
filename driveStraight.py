import mraa
import time

x = mraa.Pwm(9)	    #motor B
x.period_us(700)
x.enable(True)
y = mraa.Pwm(3)	    #motor A
y.period_us(700)
y.enable(True)

def driveForward():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(0)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(0)   #1 makes left wheel go backwards
    
    x.write(.3)
    y.write(.3)
    time.sleep(2.5)
    x.write(0)
    y.write(0)

def driveBackward():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(1)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(1)   #1 makes left wheel go backwards

    x.write(.5)
    y.write(.5)
    time.sleep(.5)
    x.write(0)
    y.write(0)

def brake():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(1)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(1)   #1 makes left wheel go backwards

    x.write(1)
    y.write(1)
    time.sleep(.04)
    x.write(1)
    y.write(1)
    time.sleep(.04)
    x.write(0)
    y.write(0)
    

driveForward()
brake()






    
