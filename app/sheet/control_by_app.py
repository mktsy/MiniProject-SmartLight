import time
import datetime

from database.vault_for_app import(
        checkStateApp,
        checkColorApp,
        checkTimeOnHour,
        checkTimeOnMin,
        checkTimeOffHour,
        checkTimeOffMin,
        checkTimeOnState,
        checkTimeOffState
)
from database.vault import(
        checkState
)
from sheet.command_function import(
        ControlLight
)


pinList_front = [4, 17, 27, 22] # red, green, blue, white 
front_light = ControlLight("Front", 1, pinList_front)# (name, light_number, GPIO)

pinList_living_room = [10, 9, 11, 0]
living_room_light = ControlLight("Living room", 2, pinList_living_room)

pinList_bedroom = [5, 6, 13, 19]
bedroom_light = ControlLight("Bedroom", 3, pinList_bedroom)

pinList_kitchen = [26, 21, 20, 16]
kitchen_light = ControlLight("Kitchen", 4, pinList_kitchen)

pinList_toilet = [12, 1, 7, 8]
toilet_light = ControlLight("Toilet", 5, pinList_toilet)

pinList_backyard = [25, 24, 23, 18]
backyard_light = ControlLight("Backyard", 6, pinList_backyard)


# create variable for light number

light_number = [1, 2, 3, 4, 5, 6]
light_list = [front_light, living_room_light, bedroom_light, kitchen_light, toilet_light, backyard_light]


def runControlLightByApp():
    try:
        while True:
            for i in light_number:
                if(checkStateApp(i) == True and checkColorApp(i) == 'off'):
                    light_list[i-1].lightOn()
                if(checkColorApp(i) == 'red'):
                    light_list[i-1].changeColorRed()
                if(checkColorApp(i) == 'green'):
                    light_list[i-1].changeColorGreen()
                if(checkColorApp(i) == 'blue'):
                    light_list[i-1].changeColorBlue()
                if(checkColorApp(i) == 'white'):
                    light_list[i-1].changeColorWhite()
                if(checkStateApp(i) == False):
                    light_list[i-1].lightOff()
     
    except KeyboardInterrupt:
        print(" Force quit...")


def runSetTime():
    try:
        while True:
            for i in light_number:
                hour_on = checkTimeOnHour(i)
                min_on = checkTimeOnMin(i)
                hour_off = checkTimeOffHour(i)
                min_off = checkTimeOffMin(i)
                time_on = [hour_on, min_on]
                time_off = [hour_off, min_off]
                now = datetime.datetime.now()
                time_now = [now.hour, now.minute]

                if(checkTimeOnState(i) == True):
                    if(time_on == time_now and checkState(i) == False):
                        light_list[i-1].lightOn()
                if(checkTimeOffState(i) == True):
                    if(time_off == time_now and checkState(i) == True):
                        light_list[i-1].lightOff()
    
    except KeyboardInterrupt:
        print("Force quit...")


time.sleep(1)





