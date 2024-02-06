import RPi.GPIO as GPIO
import time

buzzer = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(90.0)

scale = [523, 587, 659, 698, 784, 880, 988, 1047]
pongdang = [1, 2, 3, 3, 1, 3, 5, 6, 5, \
	1, 2, 3, 3, 1, 3, 5, 6, 5, \
	6, 5, 3, 6, 5, 3, 2, 2, 1, 2, 3, 5, 5, \
	6, 6, 5, 6, 8, 8, 8, 5, 5, 3, 2, 1, \
	2, 3, 1, 3, 5, 5, 5, 2, 3, 4, 3, 2, 1]

try:
	for i in range(0, 56):
		pwm.ChangeFrequency(scale[pongdang[i]-1])
		if i==8 or i==17 or i==30 or i==42 or i==55:
			time.sleep(1.0)
		else:
			time.sleep(0.5)
	pwm.stop()

finally:
	GPIO.cleanup()
