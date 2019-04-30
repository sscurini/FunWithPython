
import os
import sys

clear = lambda: os.system('cls') #Note this is the clear for windows machines. For Linux use clear=lambda: os.system('clear') 

def printLoop():
    buttonAction = "OFF" #Change this to ON or OFF and run
    isButtonONOFF = "NO" 
    while True:    
        if buttonAction == "ON" and isButtonONOFF == "NO":
            clear()
            print("The button is On")
            isButtonONOFF = "YES"            
        elif buttonAction == "OFF" and isButtonONOFF == "NO":
            clear()
            print("The button is OFF")
            isButtonONOFF = "YES"
        

printLoop() 