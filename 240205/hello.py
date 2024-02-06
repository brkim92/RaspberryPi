from flask import Flask # 플라스크 모듈 호출

app = Flask(__name__) # 플라스크 앱 생성

@app.route('/') # 기본('/') 웹 주소로 요청이 오면
def hello(): # hello 함수 실행
	return 'Hello world'

if __name__ == '__main__': # 현재 파일 실행 시 개발용 웹 서버 구동
	app.run(debug=True, port=80, host='0.0.0.0')
