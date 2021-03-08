import speech_recognition as sr
import time
import RPi.GPIO as GPIO
import datetime
from time import ctime
from pymongo import MongoClient

# Setup 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r = sr.Recognizer() # import recognizer

# Setup Database

#connection = MongoClient() # Connection with MongoClient port 27017
#db = connection.test_time # Create database test_time


pinList = [4, 17, 27, 22, 23, 24, 25, 8]
# GPIO 17, 24 = RED
# GPIO 27, 25 = GREEN
# GPIO 22, 5 = BLUE
# GPIO 23, 6 = WHITE

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

# Function input voice data

def record_audio():
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
    if 'light on' in voice_data:
        lightOnCm()
    if 'light off' in voice_data:
        lightOffCm()
    if 'frontyard' in voice_data:
        controlLightFrontyard(voice_data)
    if 'bedroom' in voice_data:
        controlLightBedroom(voice_data)
    if 'what is your name' in voice_data or "what's your name" in voice_data:
        print("My name is IANAR")
    if 'what time is it' in voice_data:
        print(ctime())
    if 'exit' in voice_data:
        exit()

# Function control light frontyard

def controlLightFrontyard(voice_data):
    if 'light on' in voice_data:
        try:
            GPIO.output(23, GPIO.HIGH)
    
    # End program cleanly with keyboard
        except KeyboardInterrupt:
            print("  Quit")

    # Reset GPIO settings
            GPIO.cleanup()

    if 'red' in voice_data:
        pinList = [27, 22, 23]
        try:
            GPIO.output(17, GPIO.HIGH)
            for i in pinList:
                GPIO.output(i, GPIO.LOW)

        except KeyboardInterrupt:
            print("  Quit")
            GPIO.cleanup()

    if 'blue' in voice_data:
        pinList = [17, 27, 23]
        try:
            GPIO.output(22, GPIO.HIGH)
            for i in pinList:
                GPIO.output(i, GPIO.LOW)

        except KeyboardInterrupt:
            print("  Quit")
            GPIO.cleanup()

    if 'green' in voice_data:
        pinList = [17, 22, 23]
        try:
            GPIO.output(27, GPIO.HIGH)
            for i in pinList:
                GPIO.output(i, GPIO.LOW)

        except KeyboardInterrupt:
            print("  Quit")
            GPIO.cleanup()

# Function control light bedroom

def controlLightBedroom(voice_data):
    if 'light on' in voice_data:
        try:
            GPIO.output(6, GPIO.HIGH)
    
    # End program cleanly with keyboard
        except KeyboardInterrupt:
            print("  Quit")

    # Reset GPIO settings
            GPIO.cleanup()

    if 'red' in voice_data:
        pinList = [25, 5, 6]
        try:
            GPIO.output(24, GPIO.HIGH)
            for i in pinList:
                GPIO.output(i, GPIO.LOW)

        except KeyboardInterrupt:
            print("  Quit")
            GPIO.cleanup()

    if 'blue' in voice_data:
        pinList = [24, 25, 6]
        try:
            GPIO.output(5, GPIO.HIGH)
            for i in pinList:
                GPIO.output(i, GPIO.LOW)
        except KeyboardInterrupt:
            print("  Quit")
            GPIO.cleanup()

    if 'green' in voice_data:
        pinList = [24, 5, 6]
        try:
            GPIO.output(25, GPIO.HIGH)
            for i in pinList:
                GPIO.output(i, GPIO.LOW)

        except KeyboardInterrupt:
            print("  Quit")
            GPIO.cleanup()

# Function control light on 

def lightOnCm():
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
    print ("turn on the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print ("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()

# Function control light off

def lightOffCm(): 
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)

    print ("turn off the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print ("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()


# Function set on-off time

def setTime():
    hour_on = 22
    minute_on = 28
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
        
while True:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
    setTime()
