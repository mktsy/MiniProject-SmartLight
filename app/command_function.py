import time
import RPi.GPIO as GPIO
import datetime
from time import ctime
import asyncio
import timeit

from database.vault import(
        update_one_value,
        check_state,
        check_color,
        check_cal_time,
        check_total_time
)


pinList = [4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26, 21, 20, 16, 12, 1, 7, 8, 25, 24, 23, 18]
light_number = [1, 2, 3, 4, 5, 6]

# Function control light on

def offLight():
    for i in pinList:
        GPIO.output(i, GPIO.LOW)

def lightOnCm():
    try:
        offLight()
        pinList_white = [11, 0, 20, 16, 23, 18]

        for i in pinList_white:
            GPIO.output(i, GPIO.HIGH)

        for i in light_number:
            old_value = {"lightNumber": i}
            new_value = {"$set": 
                    {"state": "1", 
                     "color": "white", 
                     "startTime": datetime.datetime.now(),
                     "calTime_start": timeit.default_timer()}}
            check_update = 0
            check_light_state = check_state(i)
            if(check_light_state == '0'):
                asyncio.run(update_one_value(old_value, new_value))
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

def changeColorRed():
    try:
        offLight()
        pinList_red = [4, 17, 5, 6, 12, 1]
        check_light_state = 1
        
        for i in light_number:
            if(check_state(i) != '1'):
                check_light_state = 0


        if(check_light_state == 1):
            for i in pinList_red:
                GPIO.output(i, GPIO.HIGH)

            for i in light_number:
                old_value = {"lightNumber": i}
                new_value = {"$set": {"color": "red"}}
                asyncio.run(update_one_value(old_value, new_value))

            print("Output: Change color Red")
        else:
            print("Output: Light is still off")

    
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()

# Function change all green color of light

def changeColorGreen():
    try:
        offLight()
        pinList_green = [27, 22, 13, 19, 7, 8]
        check_light_state = 1

        for i in light_number:
            if(check_state(i) != '1'):
                check_light_state = 0
        
        if(check_light_state == 1):
            for i in pinList_green:
                GPIO.output(i, GPIO.HIGH)

            for i in light_number:
                old_value = {"lightNumber": i}
                new_value = {"$set": {"color": "green"}}
                asyncio.run(update_one_value(old_value, new_value))

            print("Output: Change color Green")
        else:
            print("Output: Light is still off")

    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()

# Function change all blue color of light

def changeColorBlue():
    try:
        offLight()
        pinList_blue = [10, 9, 26, 21, 25, 24]
        check_light_state = 1
        
        for i in light_number:
            if(check_state(i) != '1'):
                check_light_state = 0

        if(check_light_state == 1):
            for i in pinList_blue:
                GPIO.output(i, GPIO.HIGH)

            for i in light_number:
                old_value = {"lightNumber": i}
                new_value = {"$set": {"color": "blue"}}
                asyncio.run(update_one_value(old_value, new_value))

            print("Output: Change color Blue")
        else:
            print("Output: Light is still off")
    
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()


# Function control light off

def lightOffCm(): 
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
        
        for i in light_number:
            start = check_cal_time(i)
            total_time = check_total_time(i)
            update_total_time = (timeit.default_timer() - start) + total_time
            old_value = {"lightNumber": i}
            new_value = {"$set": 
                            {"state": "0", 
                             "color": "off",
                             "endTime": datetime.datetime.now(),
                             "totalTime": update_total_time}}

            check_update_complete = 0
            check_light_state = check_state(i)
            if(check_light_state == '1'):
                asyncio.run(update_one_value(old_value, new_value))
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
