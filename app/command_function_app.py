import time
import RPi.GPIO as GPIO
import datetime
import asyncio
import timeit

from database.vault import(
        checkState,
        checkColor,
        checkTimeOnHour,
        checkTimeOnMin,
        checkTimeOffHour,
        checkTimeOffMin
)
from command_function import(
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
front = 1
living_room = 2
bedroom = 3
kitchen = 4
toilet = 5
backyard = 6


def controlLightByApp():
    if(checkState(front) == '1'):
        front_light.lightOn()
    if(checkColor(front) == 'red'):
        fron_light.changeColorRed()
    if(checkColor(front) == 'green'):
        front_light.changeColorGreen()
    if(checkColor(front) == 'blue'):
        front_light.changeColorBlue()
    if(checkState(front) == '0'):
        front_lightOff()




