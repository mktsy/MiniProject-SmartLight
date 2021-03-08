import speech_recognition as sr
import time
import RPi.GPIO as GPIO
import datetime
from time import ctime
from pymongo import MongoClient

# Setup GPIO & speech recognition model 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r = sr.Recognizer()

# Setup Database

#connection = MongoClient() # Connection with MongoClient port 27017
#db = connection.test_time # Create database test_time


pinList = [4, 17, 27, 22, 23, 24, 25, 8]
#  4, 23 = red
# 17, 24 = green
# 27, 25 = blue
# 22, 8  = white
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
    if 'turn on the light' in voice_data:
        lightOnCm()
    if 'turn off the light' in voice_data:
        lightOffCm()
    if 'change color red' in voice_data:
        changeColorRed()
    if 'change color green' in voice_data:
        changeColorGreen()
    if 'change color blue' in voice_data:
        changeColorBlue()
    if 'what is your name' in voice_data or "what's your name" in voice_data:
        print("My name is IANAR")
    if 'what time is it' in voice_data:
        print(ctime())
    if 'exit' in voice_data:
        exit()

# Function control light on

def lightOnCm():
    pinList = [4, 17, 27, 23, 24, 25]
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        print("turn on the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()

# Function change all red color of light

def changeColorRed():
    pinList = [17, 27, 22, 24, 25, 8]
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        print("Change color Red")
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()

# Function change all green color of light

def changeColorGreen():
    pinList = [4, 27, 22, 23, 25, 8]
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()

# Function change all blue color of light

def changeColorBlue():
    pinlist = [4, 17, 22, 23, 24, 8]
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
    except KeyboardInterrupt:
        print("  Quit")
        GPIO.cleanup()


# Function control light off

def lightOffCm(): 
    try:
        for i in pinList:
            GPIO.output(i, GPIO.LOW)
        print("turn off the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()

# Function control light frontyard

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
