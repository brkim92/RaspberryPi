from flask import Flask

app = Flask(__name__)

@app.route('/') # 기본 주소로 접속되었을 때 실행할 함수 지정
def hello():
	return 'Hello world'

@app.route('/about') # '/about'으로 접속되었을 때 실행할 함수 지정
def about():
	return 'This is about page'

@app.route('/contact') # '/contact'으로 접속되었을 때 실행할 함수 지정
def contact():
	return 'This is contact page'


if __name__ == '__main__': # 웹 서버 구동
	app.run(debug=True, port=80, host='0.0.0.0')
