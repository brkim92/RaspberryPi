import RPi.GPIO as GPIO
import time
import random

led_r = 4
led_g = 5
led_b = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_r, GPIO.OUT)
GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_b, GPIO.OUT)

def random_led_pattern():
    colors = ['red', 'green', 'blue']
    pattern = random.choices(colors, k=6)
    return pattern

def light_on_led_pattern(pattern, duration):
    for color in pattern:
        if color == 'red':
            GPIO.output(led_r, GPIO.HIGH)
        elif color == 'green':
            GPIO.output(led_g, GPIO.HIGH)
        elif color == 'blue':
            GPIO.output(led_b, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_r, GPIO.LOW)
        GPIO.output(led_g, GPIO.LOW)
        GPIO.output(led_b, GPIO.LOW)
        time.sleep(1)
    time.sleep(duration)

def display_original_pattern(pattern):
    print(f"������ {pattern} �Դϴ�.")

def compare_patterns(player_pattern, original_pattern):
    return player_pattern == original_pattern

def correct_led_pattern():
    for i in range(3):
        GPIO.output(led_g, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_g, GPIO.LOW)
        time.sleep(0.5)

def wrong_led_pattern():
    for i in range(3):
        GPIO.output(led_r, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_r, GPIO.LOW)
        time.sleep(0.5)

def play_game():
    print("�ȳ��ϼ��� LED ���� �ϱ� �׽�Ʈ�Դϴ�.")
    input("�ƹ� Ű�� ������ �����մϴ�.")
    
    original_pattern = random_led_pattern()
    
    print("������ ����ϼ���!")
    light_on_led_pattern(original_pattern, 6)
    
    player_pattern = input("������ �Է��ϼ��� (��: red green blue red blue green): ").split()
    
    if compare_patterns(player_pattern, original_pattern):
        print("�����Դϴ�!")
        correct_led_pattern()
    else:
        print("�����Դϴ�.")
        wrong_led_pattern()
        display_original_pattern(original_pattern)

    GPIO.cleanup()

# ���� �÷���
play_game()