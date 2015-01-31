import mraa
import time

x = mraa.Pwm(9)	    #motor B
x.period_us(700)
x.enable(True)
y = mraa.Pwm(3)	    #motor A
y.period_us(700)
y.enable(True)
door = mraa.Pwm(5)  #door servo
door.period_ms(20)
door.enable(True)
door.pulsewidth_us(1300) #keeps door closed while carrying balls

def flashIR():
    ir = mraa.Gpio(13)
    ir.dir(mraa.DIR_OUT)
    a = 10
    while a>0:
        ir.write(1)   
        time.sleep(1)	#Blast IR for one second		   
        ir.write(0)    
        time.sleep(2)   # Wait for the ball to fall in
        a -= 1			# do this 10 times to get all 10 balls

def driveForward():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(0)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(0)   #1 makes left wheel go backwards
    
    x.write(1)
    y.write(1)
    time.sleep(.1)
    x.write(0)
    y.write(0)

def driveBackward():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(1)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(1)   #1 makes left wheel go backwards

    x.write(1)
    y.write(1)
    time.sleep(.1)
    x.write(0)
    y.write(0)

#for turning left
def turnLeft():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(0)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(1)   #1 makes left wheel go backwards

    x.write(1)
    y.write(1)
    time.sleep(.05)
    x.write(0)
    y.write(0)

#for turning right
def turnRight():
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(1)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(0)   #1 makes left wheel go backwards

    x.write(1)
    y.write(1)
    time.sleep(.05)
    x.write(0)
    y.write(0)

#code for door
def doorClose():
    door.pulsewidth_us(1300)
    time.sleep(5)
    
def doorOpen():
    door.pulsewidth_us(2000)
    time.sleep(5)

while True:
    choose= raw_input('Input something: ')
    choose= str(choose)
    if choose=='a':
        turnLeft()
    elif choose=='w':
        driveForward()
    elif choose=='d':
        turnRight()
    elif choose=='s':
        driveBackward()
    elif choose=='j':
        doorClose()
    elif choose=='k':
        doorOpen()
    else:
        pass
    
    
