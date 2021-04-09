import speech_recognition as sr
import RPi.GPIO as GPIO
import time

from command_function import(
    allLightOn,
    changeAllColorRed,
    changeAllColorGreen,
    changeAllColorBlue,
    allLightOff,
    ControlLight
    
)
from command_function_app import(
    controlLightByApp
)

# Setup speech recognition model 

r = sr.Recognizer()

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



# Function input voice data

def recordAudio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand")
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

# Function control voice data

def respond(voice_data):
    if 'turn on the light' in voice_data:
        allLightOn()
    elif 'change color red' in voice_data:
        changeAllColorRed()
    elif 'change color green' in voice_data:
        changeAllColorGreen()
    elif 'change color blue' in voice_data:
        changeAllColorBlue()
    elif 'turn off the light' in voice_data:
        allLightOff()

    elif 'front light on' in voice_data:
        front_light.lightOn()
    elif 'front light red' in voice_data:
        front_light.changeColorRed()
    elif 'front light green' in voice_data:
        front_light.changeColorGreen()
    elif 'front light blue' in voice_data:
        front_light.changeColorBlue()
    elif 'front light off' in voice_data:
        front_light.lightOff()

    elif 'living room on' in voice_data:
        living_room_light.lightOn()
    elif 'living room red' in voice_data:
        living_room_light.changeColorRed()
    elif 'living room green' in voice_data:
        livingroom_light.changeColorGreen()
    elif 'living room blue' in voice_data:
        livingroom_light.changeColorBlue()
    elif 'living room off' in voice_data:
        livingroom_light.lightOff()
    
    elif 'bedroom on' in voice_data:
        bedroom_light.lightOn()
    elif 'bedroom red' in voice_data:
        bedroom_light.changeColorRed()
    elif 'bedroom green' in voice_data:
        bedroom_light.changeColorGreen()
    elif 'bedroom blue' in voice_data:
        bedroom_light.changeColorBlue()
    elif 'bedroom off' in voice_data:
        bedroom_light.lightOff()
    
    elif 'kitchen on' in voice_data:
        kitchen_light.lightOn()
    elif 'kitchen red' in voice_data:
        kitchen_light.changeColorRed()
    elif 'kitchen green' in voice_data:
        kitchen_light.changeColorGreen()
    elif 'kitchen blue' in voice_data:
        kitchen_light.changeColorBlue()
    elif 'kitchen off' in voice_data:
        kitchen_light.lightOff()
    
    elif 'toilet on' in voice_data:
        toilet_light.lightOn()
    elif 'toilet red' in voice_data:
        toilet_light.changeColorRed()
    elif 'toilet green' in voice_data:
        toilet_light.changeColorGreen()
    elif 'toilet blue' in voice_data:
        toilet_light.changeColorBlue()
    elif 'toilet off' in voice_data:
        toilet_light.lightOff()

    elif 'backyard on' in voice_data:
        backyard_light.lightOn()
    elif 'backyard red' in voice_data:
        backyard_light.changeColorRed()
    elif 'backyard green' in voice_data:
        backyard_light.changeColorGreen()
    elif 'backyard blue' in voice_data:
        backyard_light.changeColorBlue()
    elif 'backyard off' in voice_data:
        backyard_light.lightOff()

    elif 'exit' in voice_data:
        exit()



# Function set on-off time (inprogress)

def setTime():
    hour_on = 22
    minute_on = 28
    hour_off = 22
    minute_off = 29
    now = datetime.datetime.now()
    hour_off = 22
    minute_off = 29
    now = datetime.datetime.now()
    timeon = now.hour == hour_on and now.minute == minute_on and now.second > 0 and now.second < 5
    timeoff = now.hour == hour_off and now.minute == minute_off and now.second > 0 and now.second < 5
    if(timeon):
        lightOnCm()
    if(timeoff):
        lightOffCm()
        
time.sleep(1)

try:
    while True:
        voice_data = recordAudio()
        print("Input voice: " + voice_data)
        respond(voice_data)
        print("")

        controlLightByApp()

# End program cleanly with keyboard
except KeyboardInterrupt:
    print(" Force quit...")
