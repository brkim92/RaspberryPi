from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red_pin = 14
green_pin = 15
blue_pin = 18
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

app = Flask(__name__)


@app.route('/')
def hello():
	return "LED 제어를 위해 주소창을 변경하세요"

@app.route('/red_on') # IP주소:port/red_on 을 입력하면 나오는 페이지
def red_on(): # 해당 페이지의 뷰함수 정의
	GPIO.output(red_pin, GPIO.HIGH) # 빨간 LED 핀에 HIGH 신호 인가(LED 켜짐)
	return "red LED on" # 뷰함수의 리턴값

@app.route('/green_on') # IP주소:port/green_on 을 입력하면 나오는 페이지
def green_on(): # 해당 페이지의 뷰함수 정의
	GPIO.output(green_pin, GPIO.HIGH) # 초록 LED 핀에 HIGH 신호 인가(LED 켜짐)
	return "green LED on" 

@app.route('/blue_on') 
def blue_on(): 
	GPIO.output(blue_pin, GPIO.HIGH)
	return "blue LED on" 

@app.route('/off') # IP주소:port/off 를 입력하면 나오는 페이지
def off(): # 해당 페이지의 뷰함수 정의
	GPIO.output(red_pin, GPIO.LOW) # 각각의 LED핀에 LOW 신호를 인가하여 LED 끔
	GPIO.output(green_pin, GPIO.LOW) 
	GPIO.output(blue_pin, GPIO.LOW) 
	return "all LED off" 

@app.route('/clean_up') 
def clean_up(): 
	GPIO.cleanup()
	return "clean up" 

if __name__ == "__main__": # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
	app.run(host="192.168.0.11", port = "80")
# host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
# 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능
