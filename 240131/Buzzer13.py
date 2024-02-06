import RPi.GPIO as GPIO
import time

buzzer = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(90.0)

scale = [523, 587, 659, 698, 784, 880, 988, 1047]
frog = [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 1, \
    2, 2, 2, 2, 2, 3, 4, 3, 4, 3, 2, 1, \
    2, 2, 2, 3, 4, 3, 2, 3, 3, 3, 7, 5, \
    2, 2, 2, 3, 4, 3, 2, 3, 2, 3, 6, 5, \
    8, 8, 8, 8, 8, 5, 3, 2, 3, 4, 5, 6, \
    5, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8]

try:
    for i in range(0, 60):
        pwm.ChangeFrequency(scale[frog[i]-1])
        if i == 6 or i == 11 or i == 18 or i == 23 or i == 30 or i == 35 or i == 42 or i == 47 or i == 54 or i == 59 or i == 66 or i == 71 or i == 78 or i == 83:
            time.sleep(1.0)
        else:
            time.sleep(0.5)
    pwm.stop()

finally:
    GPIO.cleanup()