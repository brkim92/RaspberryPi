import RPi.GPIO as GPIO
import time

buzzer = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(90.0)

scale = [523, 587, 659, 698, 784, 880, 988, 1047]
mother = [3, 4, 5, 8, 8, 7, 6, 5, 6, 5, 5, 4, 3, 2, \
	3, 4, 5, 8, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1, \
	2, 2, 5, 4, 3, 2, 1, 2, 3, 3, 4, 5, 6, 5, \
	8, 8, 7, 6, 5, 6, 5, 3, 6, 6, 5, 6, 7, 8]

try:
	for i in range(0, 56):
		pwm.ChangeFrequency(scale[mother[i]-1])
		if i==7 or i ==13 or i==21 or i==35 or i==41:
			time.sleep(1.0)
		else:
			time.sleep(0.5)
	pwm.stop()

finally:
	GPIO.cleanup()
