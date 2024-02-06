import RPi.GPIO as GPIO
import time

led_pin = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

def turn_on():
	GPIO.output(led_pin, True)

def turn_off():
	GPIO.output(led_pin, False)

def fade_in():
	while True:
		for i in range(1, 30):
			GPIO.output(led_pin, True)
			time.sleep(i*0.001)
			GPIO.output(led_pin, False)
			time.sleep((30-i)*0.001)

def fade_out():
	while True:
		for i in range(1, 30):
			GPIO.output(led_pin, True)
			time.sleep((30-i)*0.001)
			GPIO.output(led_pin, False)
			time.sleep(i*0.001)

def fade_in_out_3s():
	while True:
		for i in range(1, 30):
			GPIO.output(led_pin, True)
			time.sleep(i*0.001)
			GPIO.output(led_pin, False)
			time.sleep((30-i)*0.001)
		for i in range(1, 30):
			GPIO.output(led_pin, True)
			time.sleep((30-i)*0.001)
			GPIO.output(led_pin, False)
			time.sleep(i*0.001)

def fade_in_out_free(seconds):
	while True:
		for i in range(1, seconds):
			GPIO.output(led_pin, True)
			time.sleep(i*0.001)
			GPIO.output(led_pin, False)
			time.sleep((seconds-i)*0.001)
		for i in range(1, seconds):
			GPIO.output(led_pin, True)
			time.sleep((seconds-i)*0.001)
			GPIO.output(led_pin, False)
			time.sleep(i*0.001)

while True:
	print("1. LED 켜기")
	print("2. LED 끄기")
	print("3. LED 3초간 점점 밝기")
	print("4. LED 3초간 점점 어둡기")
	print("5. LED 3초간 점점 밝다가 3초간 점점 어두워지기")
	print("6. 원하는 초 입력")
	choice = int(input("원하는 기능 : "))

	if choice == 1:
		turn_on()
	elif choice == 2:
		turn_off()
	elif choice == 3:
		 fade_in()
	elif choice == 4:
		fade_out()
	elif choice == 5:
		fade_in_out_3s()
	elif choice == 6:
		seconds = int(input("원하는 초 : "))
		fade_in_out_free(seconds)

GPIO.cleanup()
