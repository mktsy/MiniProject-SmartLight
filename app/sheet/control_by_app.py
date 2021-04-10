import time

from database.vault_for_app import(
        checkState,
        checkColor,
        checkTimeOnHour,
        checkTimeOnMin,
        checkTimeOffHour,
        checkTimeOffMin
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
front = 1
living_room = 2
bedroom = 3
kitchen = 4
toilet = 5
backyard = 6


def runControlLightByApp():
    try:
        while True:    
            if(checkState(front) == '1' and checkColor(front) == 'off'):
                front_light.lightOn()
            if(checkColor(front) == 'red'):
                front_light.changeColorRed()
            if(checkColor(front) == 'green'):
                front_light.changeColorGreen()
            if(checkColor(front) == 'blue'):
                front_light.changeColorBlue()
            if(checkColor(front) == 'white'):
                front_light.changeColorWhite()
            if(checkState(front) == '0'):
                front_light.lightOff()
    
            if(checkState(living_room) == '1' and checkColor(living_room) == 'off'):
                living_room_light.lightOn()
            if(checkColor(living_room) == 'red'):
                living_room_light.changeColorRed()
            if(checkColor(living_room) == 'green'):
                living_room_light.changeColorGreen()
            if(checkColor(living_room) == 'blue'):
                living_room_light.changeColorBlue()
            if(checkColor(living_room) == 'white'):
                living_room_light.changeColorWhite()
            if(checkState(living_room) == '0'):
                living_room_light.lightOff()

            if(checkState(bedroom) == '1' and checkColor(bedroom) == 'off'):
                bedroom_light.lightOn()
            if(checkColor(bedroom) == 'red'):
                bedroom_light.changeColorRed()
            if(checkColor(bedroom) == 'green'):
                bedroom_light.changeColorGreen()
            if(checkColor(bedroom) == 'blue'):
                bedroom_light.changeColorBlue()
            if(checkColor(bedroom) == 'white'):
                bedroom_light.changeColorWhite()
            if(checkState(bedroom) == '0'):
                bedroom_light.lightOff()

            if(checkState(kitchen) == '1' and checkColor(kitchen) == 'off'):
                kitchen_light.lightOn()
            if(checkColor(kitchen) == 'red'):
                kitchen_light.changeColorRed()
            if(checkColor(kitchen) == 'green'):
                kitchen_light.changeColorGreen()
            if(checkColor(kitchen) == 'blue'):
                kitchen_light.changeColorBlue()
            if(checkColor(kitchen) == 'white'):
                kitchen_light.changeColorWhite()
            if(checkState(kitchen) == '0'):
                kitchen_light.lightOff()

            if(checkState(toilet) == '1' and checkColor(toilet) == 'off'):
                toilet_light.lightOn()
            if(checkColor(toilet) == 'red'):
                toilet_light.changeColorRed()
            if(checkColor(toilet) == 'green'):
                toilet_light.changeColorGreen()
            if(checkColor(toilet) == 'blue'):
                toilet_light.changeColorBlue()
            if(checkColor(toilet) == 'white'):
                toilet_light.changeColorWhite()
            if(checkState(toilet) == '0'):
                toilet_light.lightOff()

            if(checkState(backyard) == '1' and checkColor(backyard) == 'off'):
                backyard_light.lightOn()
            if(checkColor(backyard) == 'red'):
                backyard_light.changeColorRed()
            if(checkColor(backyard) == 'green'):
                backyard_light.changeColorGreen()
            if(checkColor(backyard) == 'blue'):
                backyard_light.changeColorBlue()
            if(checkColor(backyard) == 'white'):
                backyard_light.changeColorWhite()
            if(checkState(backyard) == '0'):
                backyard_light.lightOff()

    except KeyboardInterrupt:
        print(" Force quit...")

time.sleep(1)





