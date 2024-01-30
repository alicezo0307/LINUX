import RPi.GPIO as GPIO
import time
import drivers
from time import sleep

display = drivers.Lcd()
display.lcd_clear()
SW1  = 27  
SW2  = 17
i=0
j=12
space = " "

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

try:
    while True:
            if GPIO.event_detected(SW1):
                  i +=1
                  j -=1
            
            elif GPIO.event_detected(SW2):
                  j +=1
                  i -=1
               
            if(i>=12):
               i=12
            if(j<=0):
               j=0
            display.lcd_display_string((space*i)+"LAB7"+(space*j), 1)
            
except KeyboardInterrupt:
   GPIO.remove_event_detect(SW1)
   GPIO.remove_event_detect(SW2)
   GPIO.cleanup()
   print("\nBye...")

