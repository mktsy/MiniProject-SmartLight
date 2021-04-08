import time
import RPi.GPIO as GPIO
import datetime
from time import ctime
import asyncio
import timeit

from database.vault import(
        updateOneValue,
        checkState,
        checkColor,
        checkCalTime,
        checkTotalTime
)

# set mode and close warning GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26, 21, 20, 16, 12, 1, 7, 8, 25, 24, 23, 18] # raspberry pi GPIO
light_number = [1, 2, 3, 4, 5, 6] # 6 light bulbs

for i in pinList:
    GPIO.setup(i, GPIO.OUT)


class ControlLight:
    def __init__(self, name, light_number, pinList):
        self.name = name
        self.light_number = light_number
        self.pinList = pinList
    
    def lightOn(self):
        for i in self.pinList:
            GPIO.output(self.pinList, GPIO.LOW)
        GPIO.output(self.pinList[3], GPIO.HIGH)

        old_value = {"lightNumber": self.light_number}
        new_value = {"$set": 
                        {"state": "1", 
                         "color": "white",
                         "startTime": datetime.datetime.now(),
                         "calTime_start": timeit.default_timer()}}

        if(checkState(self.light_number) == '0'):
            asyncio.run(updateOneValue(old_value, new_value))
            print("Database updated.")

        print("Output: " + self.name + " light on")
    
    def lightOff(self):
        for i in self.pinList:
            GPIO.output(i, GPIO.LOW)
        
        start = checkCalTime(self.light_number)
        total_time = checkTotalTime(self.light_number)
        update_total_time = (timeit.default_timer() - start) + total_time
        old_value = {"lightNumber": self.light_number}
        new_value = {"$set":
                        {"state": "0",
                         "color": "off",
                         "endTime": datetime.datetime.now(),
                         "totalTIme": update_total_time}}

        if(checkState(self.light_number) == '1'):
            asyncio.run(updateOneValue(old_value, new_value))
            print("Database updated.")

        print("Output: " + self.name + " light off")

    def changeColorRed(self):
        if(checkState(self.light_number) == '1'):
            for i in self.pinList:
                GPIO.output(i, GPIO.LOW)
            GPIO.output(self.pinList[0], GPIO.HIGH)

            old_value = {"lightNumber": self.light_number}
            new_value = {"$set": {"color": "red",}}
            asyncio.run(updateOneValue(old_value, new_value))
            
            print("Database updated.")
            print("Output: " + self.name + " light change color to red")

        else:
            print("Output: Light is still off")

    def changeColorGreen(self):
        if(checkState(self.light_number) == '1'):
            for i in self.pinList:
                GPIO.output(i, GPIO.LOW)
            GPIO.output(self.pinList[1], GPIO.HIGH)

            old_value = {"lightNumber": self.light_number}
            new_value = {"$set": {"color": "green",}}
            asyncio.run(updateOneValue(old_value, new_value))
            
            print("Database updated.")
            print("Output: " + self.name + " light change color to green")

        else:
            print("Output: Light is still off")

    def changeColorBlue(self):
        if(checkState(self.light_number) == '1'):
            for i in self.pinList:
                GPIO.output(i, GPIO.LOW)
            GPIO.output(self.pinList[2], GPIO.HIGH)

            old_value = {"lightNumber": self.light_number}
            new_value = {"$set": {"color": "blue",}}
            asyncio.run(updateOneValue(old_value, new_value))
            
            print("Database updated.")
            print("Output: " + self.name + " light change color to blue")

        else:
            print("Output: Light is still off")



# Function control light on

def lightOff():
    for i in pinList:
        GPIO.output(i, GPIO.LOW)


def allLightOn():
    lightOff()
    pinList_white = [22, 0, 19, 16, 8, 18]

    for i in pinList_white:
        GPIO.output(i, GPIO.HIGH)

    for i in light_number:
        old_value = {"lightNumber": i}
        new_value = {"$set": 
                        {"state": "1", 
                         "color": "white", 
                         "startTime": datetime.datetime.now(),
                         "calTime_start": timeit.default_timer()}}
    
        check_light_state = checkState(i)
        if(check_light_state == '0'):
            asyncio.run(updateOneValue(old_value, new_value))

    print("Output: turn on the light")


# Function change all red color of light

def changeAllColorRed():
    lightOff()
    pinList_red = [4, 10, 5, 26, 12, 25]
    check_light_state = 1
        
    for i in light_number:
        if(checkState(i) != '1'): #check state of light from database
            check_light_state = 0


    if(check_light_state == 1):
        for i in pinList_red:
            GPIO.output(i, GPIO.HIGH)

        for i in light_number:
            old_value = {"lightNumber": i}
            new_value = {"$set": {"color": "red"}}
            asyncio.run(updateOneValue(old_value, new_value))
           
        print("Output: Change color Red")
    else:
        print("Output: Light is still off")

   
# Function change all green color of light

def changeAllColorGreen():
    lightOff()
    pinList_green = [17, 9, 6, 21, 1, 24]
    check_light_state = 1

    for i in light_number:
        if(checkState(i) != '1'):
            check_light_state = 0
        
    if(check_light_state == 1):
        for i in pinList_green:
            GPIO.output(i, GPIO.HIGH)

        for i in light_number:
            old_value = {"lightNumber": i}
            new_value = {"$set": {"color": "green"}}
            asyncio.run(updateOneValue(old_value, new_value))

        print("Output: Change color Green")
    else:
        print("Output: Light is still off")


# Function change all blue color of light

def changeAllColorBlue():
    lightOff()
    pinList_blue = [27, 11, 13, 20, 7, 23]
    check_light_state = 1
        
    for i in light_number:
        if(checkState(i) != '1'):
            check_light_state = 0

    if(check_light_state == 1):
        for i in pinList_blue:
            GPIO.output(i, GPIO.HIGH)

        for i in light_number:
            old_value = {"lightNumber": i}
            new_value = {"$set": {"color": "blue"}}
            asyncio.run(updateOneValue(old_value, new_value))

        print("Output: Change color Blue")
    else:
        print("Output: Light is still off")
   

# Function control light off

def allLightOff(): 
    for i in pinList:
        GPIO.output(i, GPIO.LOW)
        
    for i in light_number:
        start = checkCalTime(i)
        total_time = checkTotalTime(i)
        update_total_time = (timeit.default_timer() - start) + total_time
        old_value = {"lightNumber": i}
        new_value = {"$set": 
                        {"state": "0", 
                         "color": "off",
                         "endTime": datetime.datetime.now(),
                         "totalTime": update_total_time}}

        check_light_state = checkState(i)
        if(check_light_state == '1'):
            asyncio.run(updateOneValue(old_value, new_value))
        
    print("Output: turn off the light")
  

