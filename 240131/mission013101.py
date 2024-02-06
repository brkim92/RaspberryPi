import RPi.GPIO as GPIO
import time
import random

led_pin_red = 4
led_pin_green = 5
led_pin_blue = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)

print("-------------------------------------------------------------------")
print("RGB GAME")
print("Let's check the color and guess what color it will be when combined")
print("-------------------------------------------------------------------\n")

def getRGB():
	colors = ['red', 'green', 'blue']
	selected_colors = random.sample(colors, 2)
	return selected_colors

selected_colors = getRGB()
print(selected_colors)

print("----------------------")
print("1. yellow")
print("2. magenta")
print("3. cyan")
print("4. white")
print("----------------------\n")

answer = input("Input the number: ")

if answer == '1' and 'red' in selected_colors and 'green' in selected_colors:
	print("O!")
	GPIO.output(led_pin_red, GPIO.HIGH)
	GPIO.output(led_pin_green, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.LOW)
	GPIO.output(led_pin_green, GPIO.LOW)
	time.sleep(0.5)
elif answer == '2' and 'red' in selected_colors and 'blue' in selected_colors:
	print("O!")
	GPIO.output(led_pin_red, GPIO.HIGH)
	GPIO.output(led_pin_blue, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.LOW)
	GPIO.output(led_pin_blue, GPIO.LOW)
	time.sleep(0.5)
elif answer == '3' and 'green' in selected_colors and 'blue' in selected_colors:
	print("O!")
	GPIO.output(led_pin_green, GPIO.HIGH)
	GPIO.output(led_pin_blue, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_green, GPIO.LOW)
	GPIO.output(led_pin_blue, GPIO.LOW)
	time.sleep(0.5)
elif answer == '4' and 'red' in selected_colors and 'green' in selected_colors and 'blue' in selected_colors:
	print("O!")
	GPIO.output(led_pin_red, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_green, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_blue, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.LOW)
	GPIO.output(led_pin_green, GPIO.LOW)
	GPIO.output(led_pin_blue, GPIO.LOW)
else:
	print("X!")
	GPIO.output(led_pin_red, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(led_pin_red, GPIO.LOW)
	time.sleep(0.5)
