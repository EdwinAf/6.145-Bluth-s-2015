import mraa
import time
import math

x = mraa.Pwm(9)	    #motor B
x.period_us(700)
x.enable(True)
y = mraa.Pwm(3)	    #motor A
y.period_us(700)
y.enable(True)

#for turning left
def turnLeft(degrees):
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(0)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(1)   #1 makes left wheel go backwards

    time1= (degrees+19.667)/388.57
    x.write(1)
    y.write(1)
    time.sleep(time1)
    x.write(0)
    y.write(0)

#for turning right
def turnRight(degrees):
    dirA = mraa.Gpio(12)
    dirA.dir(mraa.DIR_OUT)
    dirA.write(1)   #1 makes right wheel go backwards

    dirB = mraa.Gpio(13)
    dirB.dir(mraa.DIR_OUT)
    dirB.write(0)   #1 makes left wheel go backwards

    time1= (degrees+19.667)/388.57
    x.write(1)
    y.write(1)
    time.sleep(time1)
    x.write(0)
    y.write(0)

def turn(angle):
    if angle<0:
        turnLeft(abs(angle))
    else:
        turnRight(angle)
    
'''    
list1=[]
list2=[]
a=0
while a<20:
    ans= raw_input('Enter a time')
    ans= float(ans)
    turnLeft(ans)
    a+=1
    angle= raw_input('Enter an angle')
    angle=int(angle)
    list1.append(ans)
    list2.append(angle)
'''

while True:
    a=raw_input('Angle?')
    a=int(a)
    turn(a)

    
x.write(0)
y.write(0)
print list1
print list2

