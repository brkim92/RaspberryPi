import RPi.GPIO as GPIO
import time
import random

SW1 = 22
SW2 = 23
SW3 = 24
Red_LED = 4
Green_LED = 5
Blue_LED = 6 

GPIO.setmode(GPIO.BCM)
# SW 핀 설정
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# LED 핀 설정
GPIO.setup(Red_LED, GPIO.OUT)
GPIO.setup(Green_LED, GPIO.OUT)
GPIO.setup(Blue_LED, GPIO.OUT)

# LED 초기화
GPIO.output(Red_LED, GPIO.LOW)
GPIO.output(Green_LED, GPIO.LOW)
GPIO.output(Blue_LED, GPIO.LOW)

# 랜덤 색 및 시간 설정
colors = ['Red', 'Green', 'Blue']
times = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

def game_round():
    # 랜덤 색, 시간 선택
    selected_color = random.choice(colors)
    selected_time = random.choice(times)

    # LED 켜기
    if selected_color == 'Red':
        GPIO.output(Red_LED, GPIO.HIGH)
    elif selected_color == 'Green':
        GPIO.output(Green_LED, GPIO.HIGH)
    elif selected_color == 'Blue':
        GPIO.output(Blue_LED, GPIO.HIGH)
    
    # 대기 시작 시간 설정
    start_time = time.time()
    
    # 불이 들어와 있는 동안 버튼을 누를 수 있는 시간 동안 체크
    while time.time() - start_time < selected_time:
        button_pressed = GPIO.input(SW1) | (GPIO.input(SW2) << 1) | (GPIO.input(SW3) << 2)
        if button_pressed in [SW1, SW2, SW3]:
            break
    
    # LED 끄기
    GPIO.output(Red_LED, GPIO.LOW)
    GPIO.output(Green_LED, GPIO.LOW)
    GPIO.output(Blue_LED, GPIO.LOW)
    
    # 판정 1, 2, 3
    if button_pressed == SW1 and selected_color == 'Red':
        print("perfect")
        return 2  # perfect인 경우 2점 반환
    elif button_pressed & SW1 == 0 and selected_color == 'Red':
        print("bad")
        return 0  # 다른 버튼을 누른 경우 0점 반환
    elif button_pressed == SW2 and selected_color == 'Green':
        print("perfect")
        return 2
    elif button_pressed & SW2 == 0 and selected_color == 'Green':
        print("bad")
        return 0
    elif button_pressed == SW3 and selected_color == 'Blue':
        print("perfect")
        return 2
    elif button_pressed & SW3 == 0 and selected_color == 'Blue':
        print("bad")
        return 0
    else:
        print("miss")
        return 0

# 메인 루프
score = 0
for i in range(10):
    score += game_round()

print(f"최종 점수는 {score}점")
    
# GPIO 정리
GPIO.cleanup()
