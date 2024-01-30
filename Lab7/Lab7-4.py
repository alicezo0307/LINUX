import RPi.GPIO as GPIO
import time
import drivers
from time import sleep

display = drivers.Lcd()
display.lcd_clear()
OutName=["Napapa Khumphuean","Thummathan Sopaboon"]
OutID=["116510400045-0","116510400046-8"]
SW1  = 27  
SW2  = 17
i=0
lcd_position = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

try:
    while True:
         while i <=1:
            if GPIO.event_detected(SW1):
                  display.lcd_display_string(OutName[i], 1)
                  display.lcd_display_string(OutID[i], 2)
                  i = i+ 1
                  
                  sleep(0.5)
                  if(i>1):
                     i=0
            
            elif GPIO.event_detected(SW2):
                  GPIO.remove_event_detect(SW1)
                  GPIO.remove_event_detect(SW2)
                  display.lcd_clear()
                  print("\nBye...")
                  break
             
except KeyboardInterrupt:
   GPIO.remove_event_detect(SW1)
   GPIO.remove_event_detect(SW2)
   GPIO.cleanup()
   print("\nBye...")

