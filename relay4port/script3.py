import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [17, 27, 22, 23]

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.2

# main loop

try:
  GPIO.output(17, GPIO.LOW) #2 = 17
  time.sleep(SleepTimeL);

  GPIO.output(27, GPIO.LOW) #3 = 27
  time.sleep(SleepTimeL);

  GPIO.output(22, GPIO.LOW) #4 = 22
  time.sleep(SleepTimeL);

  GPIO.output(27, GPIO.LOW) #17 = 23
  time.sleep(SleepTimeL);

  GPIO.output(27, GPIO.HIGH)
  GPIO.output(22, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(17, GPIO.HIGH)
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(27, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(17, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(27, GPIO.HIGH)
  GPIO.output(22, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(27, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(17, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(27, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(22, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(23, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()
