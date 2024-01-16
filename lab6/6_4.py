import RPi.GPIO as GPIO
import time
SW = 22
LEDr = 14
LEDg = 15
LEDb = 18
count = 0
n = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDr, GPIO.OUT)
GPIO.setup(LEDg, GPIO.OUT)
GPIO.setup(LEDb, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)
listRGB = [0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1]

try:
    while True :
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            count = count+1
            GPIO.output(LEDr, listRGB[n-1])
            GPIO.output(LEDg, listRGB[n])
            GPIO.output(LEDb, listRGB[n+1])
            print(listRGB[n-1] ,listRGB[n], listRGB[n+1] )
            print(n)
            n +=3
            if n > 22 :
                n = 1
            time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()


print("\nBye..")
