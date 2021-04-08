import speech_recognition as sr
import RPi.GPIO as GPIO
import time

from command_function import(
    allLightOn,
    changeAllColorRed,
    changeAllColorGreen,
    changeAllColorBlue,
    allLightOff
    
)
# Setup GPIO & speech recognition model 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
r = sr.Recognizer()


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
    if 'turn off the light' in voice_data:
        allLightOff()
    if 'red' in voice_data:
        changeAllColorRed()
    if 'green' in voice_data:
        changeAllColorGreen()
    if 'blue' in voice_data:
        changeAllColorBlue()
    if 'what is your name' in voice_data or "what's your name" in voice_data:
        print("My name is IANAR")
    if 'what time is it' in voice_data:
        print(ctime())
    if 'exit' in voice_data:
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
        
while True:
    voice_data = recordAudio()
    print("Input voice: " + voice_data)
    respond(voice_data)
