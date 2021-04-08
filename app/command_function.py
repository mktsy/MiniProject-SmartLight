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
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26, 21, 20, 16, 12, 1, 7, 8, 25, 24, 23, 18]
light_number = [1, 2, 3, 4, 5, 6]

# Function control light on

def lightOff():
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)

def allLightOn():
    try:
        lightOff()
        pinList_white = [22, 0, 19, 16, 8, 18]

        for i in pinList_white:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)

        for i in light_number:
            old_value = {"lightNumber": i}
            new_value = {"$set": 
                    {"state": "1", 
                     "color": "white", 
                     "startTime": datetime.datetime.now(),
                     "calTime_start": timeit.default_timer()}}
            check_update = 0
            check_light_state = checkState(i)
            if(check_light_state == '0'):
                asyncio.run(updateOneValue(old_value, new_value))
                check_update = 1
            if(i == 6 and check_update == 1):
                print("Database updated.")

        print("Output: turn on the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()

# Function change all red color of light

def changeAllColorRed():
    try:
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

    
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()

# Function change all green color of light

def changeAllColorGreen():
    try:
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

    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()

# Function change all blue color of light

def changeAllColorBlue():
    try:
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
    
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()


# Function control light off

def allLightOff(): 
    try:
        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
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

            check_update_complete = 0
            check_light_state = checkState(i)
            if(check_light_state == '1'):
                asyncio.run(updateOneValue(old_value, new_value))
                check_update_complete = 1
            if(i == 6 and check_update_complete == 1):
                print("Database updated.")
        
        print("Output: turn off the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()

# Function control light frontyard

def frontyardLightOn():
    pass

def frontyardChangeColorRed():
    pass
