import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pir_sensor = 27
buzzer = 14

GPIO.setup(27, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

try:
	while True:
		if GPIO.input(27):
			print("Detected")
			pwm = GPIO.PWM(buzzer, 262)
			pwm.start(50.0)
			time.sleep(1.5)
			pwm.stop()
		else:
			print ("Not Detected")
			time.sleep(0.1)

except KeyboardInterrupt:
	pass

GPIO.cleanup()
