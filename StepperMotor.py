# Stepper motor

import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22) # Define pins connected to four phase ABCD of stepper motor
CCWStep = (0x01, 0x02, 0x04, 0x08) # Define power supply order for coil for rotating counter clockwise
CWStep = (0x08, 0x04, 0x02, 0x01) # Define power supply order for coil for rotating counter clockwise

def setup():
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD) # Numbers GPIO pins by physical location
    for pin in motorPins:
        GPIO.setup(pin,GPIO.OUT) # As for 4 phase stepper motor, 4 steps are one cycle. The function is
                                 # used to drive the stepper motor CW or CCW, taking 4 steps.
                                 
def moveOnePeriod(direction, ms):
    for j in range(0,4,1):          # Cycle for power supply order
        for i in range(0,4,1):      # Assign to each pin, a total of 4 pins
            if (direction == 1):     # Power supply rotates motor CW
               GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))            
               
            else:               # Power supply rotate CCW
                GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):                   # The delay cannot be less than 3ms or it will exceed the speed limit of motor
            ms = 300
        time.sleep(ms*0.001)
        a = GPIO.input(12)
        b = GPIO.input(16)
        c = GPIO.input(18)
        d = GPIO.input(22)
        print(a, b, c, d)

# Continuous rotation function, the parameter steps specify the rotation cycles. Every 4 steps is a cycle

def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
        
# Function used to stop rotating

def motorStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i],GPIO.LOW)
        
def loop():
    while True:
        moveSteps(1,800,512) # Rotating 360 degrees CW with a total of 2048 steps in a circle, namely 512 cycles.
        time.sleep(0.5)
        moveSteps(0,800,512) # Rotating 360 degrees CCW
        time.sleep(0.5)
        
def destroy():
    GPIO.cleanup()
    
x = 1

if x == 1:
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


        

