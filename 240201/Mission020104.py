import RPi.GPIO as GPIO
import random
import time

# GPIO 핀 번호 설정
LED_PIN = [4, 5, 6]  # Red, Green, Blue
SW1 = 22
SW2 = 23
SW3 = 24
SW4 = 25
BUZZER_PIN = 14

# 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO 핀 모드 설정
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM = 100Hz
BUZZER = GPIO.PWM(BUZZER_PIN, 100)

# LED 초기화(for in range 형태)
for pin in LED_PIN:
    GPIO.output(pin, GPIO.LOW)

# 3. 시간과 컬러를 입력받아 소리를 재생하는 함수 작성(빨간색은 262Hz, 초록색은 294Hz, 파란색은 330Hz)
def play_sound(color):
    if color == 0:
        BUZZER.ChangeFrequency(262)
    elif color == 1:
        BUZZER.ChangeFrequency(294)
    elif color == 2:
        BUZZER.ChangeFrequency(330)
    BUZZER.start(50)  # 50% duty cycle
    time.sleep(0.5)
    BUZZER.stop()
    time.sleep(0.1)  # 부저 정지 후 잠시 대기

# 4. 순서배열을 입력받고 배열의 컬러값의 순서대로 LED를 켜고 소리를 내는 함수 작성 (소리를 낼때는 앞에서의 소리를 재생하는 함수 활용)
def play_sequence(sequence):
    for color in sequence:
        GPIO.output(LED_PIN[color], GPIO.HIGH)
        play_sound(color)
        GPIO.output(LED_PIN[color], GPIO.LOW)
        time.sleep(0.5)

# 5. 플레이어의 입력을 받아 값을 반환해주는 함수 작성, 특정 시퀀스의 길이만큼 플레이어에게 버튼 입력을 받아 시퀀스를 완성하는 함수
def get_player_input(length):  # The number of inputs the player
    player_input = []  # Store the player's input
    for _ in range(length):  # iterate 'length' times
        while True:  # This loop keeps running until the player makes a valid input by pressing one of the buttons
            if GPIO.input(SW1) == GPIO.HIGH:
                player_input.append(0)  # Red
                play_sound(0)  # 부저 울리기
                break
            elif GPIO.input(SW2) == GPIO.HIGH:
                player_input.append(1)  # Green
                play_sound(1)  # 부저 울리기
                break
            elif GPIO.input(SW3) == GPIO.HIGH:
                player_input.append(2)  # Blue
                play_sound(2)  # 부저 울리기
                break
    return player_input

# 6. 메인 함수를 따로 작성하고 #try-except-finally 구문을 사용하여 GPIO를 정리
def main():
    try:
        # 7. 시퀀스의 배열을 미리 만들어 준 뒤
        sequence = []
        # 무한 반복문 생성
        while True:
            for _ in range(3):  # 3 cycles
                color = random.choice(range(3))
                sequence.append(color)
                play_sequence(sequence)
                player_input = get_player_input(len(sequence))
                
                # 사용자 입력이 시퀀스와 다르면 게임 종료
                if player_input != sequence:
                    print(f"Game Over! Your score: {len(sequence) - 1}")
                    return

                # SW4 버튼을 누르면 게임 종료
                if GPIO.input(SW4) == GPIO.LOW:
                    print(f"강제 종료! Your score: {len(sequence) - 1}")  # 점수 출력
                    return

                time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
