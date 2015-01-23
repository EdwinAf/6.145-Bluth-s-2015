from wiringx86 import GPIOEdison as GPIO
import time

#Setup Code
# Create new instance of the GPIOEdison class.
# Setting debug=True gives information about the interaction with sysfs.
gpio = GPIO(debug=False)
door = 5  #pin 5 is the servo, 3 is the working motor
gpio.pinMode(door, gpio.PWM)    #setting up PWM on door

IR= 13 
gpio.pinMode(IR, gpio.OUTPUT)

def signalDisp():   # Called if current goal is not final goal
    a = 10
    while a>0:
        gpio.digitalWrite(IR ,gpio.HIGH)   #Blast IR for one second
        time.sleep(1)			   
        gpio.digitalWrite(IR, gpio.LOW)    # Wait for the ball to fall
        time.sleep(2)
        a -= 1			     # do this 10 times
	 
def doorClosed():    #function that keeps the door closed
    gpio.analogWrite(door, 0)
    print 'Door should now be closed'

def doorOpen():    #function that opens door
    gpio.analogWrite(door, 255)
    print 'Door should now be open'
    time.sleep(2)

def ballHandler():         #Called when a goal is reached       
    if len(goalList)>0:    # If not final goal activate disp
        signalDisp()
    else:                  # else open door
        print 'length==0'
        doorOpen()
        

doorOpen() 
doorClosed()   
goalList= [2]
ballHandler()
goalList= []
ballHandler()


print len(goalList)
