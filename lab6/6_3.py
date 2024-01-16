import RPi.GPIO as GPIO
import time
SW = 22
LED = 18
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True :
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            count = count+1
            GPIO.output(LED, True)
            print("on")
            while GPIO.wait_for_edge(SW, GPIO.FALLING):
                GPIO.output(LED, False)
                print("off")
                break
            
except KeyboardInterrupt:
    GPIO.cleanup()

print("\nBye..")
