import RPi.GPIO as GPIO
import time

buzzer_pin = 14
button_pin1 = 22  # SW1
button_pin2 = 23  # SW2
button_pin3 = 24  # SW3
led_red_pin = 4  # Red LED
led_green_pin = 5  # Green LED
led_blue_pin = 6  # Blue LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED 핀 설정
GPIO.setup(led_red_pin, GPIO.OUT)
GPIO.setup(led_green_pin, GPIO.OUT)
GPIO.setup(led_blue_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)
pwm.start(90.0)

scale = [523, 587, 659, 698, 784, 880, 988, 1047]

pongdang = [1, 2, 3, 3, 1, 3, 5, 6, 5,
            1, 2, 3, 3, 1, 3, 5, 6, 5,
            6, 5, 3, 6, 5, 3, 2, 2, 1, 2, 3, 5, 5,
            6, 6, 5, 6, 8, 8, 8, 5, 5, 3, 2, 1,
            2, 3, 1, 3, 5, 5, 5, 2, 3, 4, 3, 2, 1]

mother = [3, 4, 5, 8, 8, 7, 6, 5, 6, 5, 5, 4, 3, 2,
          3, 4, 5, 8, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1,
          2, 2, 5, 4, 3, 2, 1, 2, 3, 3, 4, 5, 6, 5,
          8, 8, 7, 6, 5, 6, 5, 3, 6, 6, 5, 6, 7, 8]

frog = [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 1,
        2, 2, 2, 2, 2, 3, 4, 3, 4, 3, 2, 1,
        2, 2, 2, 3, 4, 3, 2, 3, 3, 3, 7, 5,
        2, 2, 2, 3, 4, 3, 2, 3, 2, 3, 6, 5,
        8, 8, 8, 8, 8, 5, 3, 2, 3, 4, 5, 6,
        5, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8]

def check_for_esc():
    return GPIO.input(button_pin1) == GPIO.LOW

# 노래 정지 함수
def stop_melody():
    pwm.ChangeDutyCycle(0)  # Buzzer를 끄기


def play_melody1(melody):
    GPIO.output(led_red_pin, GPIO.HIGH)
    GPIO.output(led_green_pin, GPIO.LOW)
    GPIO.output(led_blue_pin, GPIO.LOW)
    
    for note in melody:
        pwm.ChangeFrequency(scale[note-1])
        if note in [9, 18, 31, 43, 56]:
            time.sleep(1.0)
        else:
            time.sleep(0.5)
            
            if check_for_esc():
            stop_melody()
            return
            
    GPIO.output(led_red_pin, GPIO.LOW)            

            
def play_melody2(melody):
    GPIO.output(led_red_pin, GPIO.LOW)
    GPIO.output(led_green_pin, GPIO.HIGH)
    GPIO.output(led_blue_pin, GPIO.LOW)
    
    for note in melody:
        pwm.ChangeFrequency(scale[note-1])
        if note in [8, 14, 22, 36, 42]:
            time.sleep(1.0)
        else:
            time.sleep(0.5)
            
            if check_for_esc():
            stop_melody()
            return
            
    GPIO.output(led_green_pin, GPIO.LOW)
            
def play_melody3(melody):
    GPIO.output(led_red_pin, GPIO.LOW)
    GPIO.output(led_green_pin, GPIO.LOW)
    GPIO.output(led_blue_pin, GPIO.HIGH)
    
    for note in melody:
        pwm.ChangeFrequency(scale[note-1])
        if note in [7, 12, 19, 24, 31, 36, 43, 48,55, 60, 67, 72, 79, 84]:
            time.sleep(1.0)
        else:
            time.sleep(0.5)
            
            if check_for_esc():
            stop_melody()
            return
            
    GPIO.output(led_blue_pin, GPIO.LOW)

try:
    while True:
        if GPIO.input(button_pin1) == GPIO.LOW:
            play_melody1(pongdang)
        elif GPIO.input(button_pin2) == GPIO.LOW:
            play_melody2(mother)
        elif GPIO.input(button_pin3) == GPIO.LOW:
            play_melody3(frog)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
