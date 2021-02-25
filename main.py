import speech_recognition as sr
import time
import RPi.GPIO as GPIO
import datetime
from time import ctime
from pymongo import MongoClient

# Setup 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r = sr.Recognizer()

# Setup Database

#connection = MongoClient() # Connection with MongoClient port 27017
#db = connection.test_time # Create database test_time


pinList = [17, 27, 22, 23]

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
    if 'what is your name' in voice_data or "what's your name" in voice_data:
        print("My name is IANAR")
    if 'what time is it' in voice_data:
        print(ctime())
    if 'exit' in voice_data:
        exit()

# Function control lgiht on

def lightOnCm(): 
    try:
      GPIO.output(17, GPIO.HIGH)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH)
      GPIO.output(23, GPIO.HIGH)
      print ("turn on the light")
      
  # End program cleanly with keyboard
    except KeyboardInterrupt:
      print ("  Quit")

  # Reset GPIO settings
      GPIO.cleanup()

# Function control light off

def lightOffCm(): 
    try:
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.LOW)
      GPIO.output(22, GPIO.LOW)
      GPIO.output(23, GPIO.LOW)
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

