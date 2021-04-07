import speech_recognition as sr
import RPi.GPIO as GPIO
import time

from command_function import(
    lightOnCm,
    changeColorRed,
    changeColorGreen,
    changeColorBlue,
    lightOffCm
    
)
# Setup GPIO & speech recognition model 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r = sr.Recognizer()


pinList = [4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26, 21, 20, 16, 12, 1, 7, 8, 25, 24, 23, 18]
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
    if 'red' in voice_data:
        changeColorRed()
    if 'green' in voice_data:
        changeColorGreen()
    if 'blue' in voice_data:
        changeColorBlue()
    if 'what is your name' in voice_data or "what's your name" in voice_data:
        print("My name is IANAR")
    if 'what time is it' in voice_data:
        print(ctime())
    if 'exit' in voice_data:
        exit()



# Function set on-off time

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
        
while True:
    voice_data = record_audio()
    print("Input voice: " + voice_data)
    respond(voice_data)
