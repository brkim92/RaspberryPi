import time
import RPi.GPIO as GPIO

led_pins = [4, 5, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)

def led():
	for pin in led_pins:
		GPIO.output(pin, True)
		time.sleep(0.5)
		GPIO.output(pin, False)

for i in range(20):
	led()
