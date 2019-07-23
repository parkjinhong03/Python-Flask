# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
# 현재 모듈에 대해 Flask 객체를 생성

@app.route('/')
# 데코레이터를 통해 '/'에 라우팅. Flask에 라우팅의 기본형
# 위의 URL에 대해 할당되어 로직을 처리하는 함수를 view function이라고 부른다
# 별도의 HTTP 메소드 명사가 없으면 GET에서 라우팅한다.
def index():
    return 'JINHONG~!'
    # 요청이 들어오면, 문자열 'Hello world'를 응답으로 전달, status code 명시X -> 200 ok로 처리


@app.route('/custom/<int:param>')
# path parameter 정의 - <type:name>, 타입 생략 가능, 그럴 경우 타입은 str로 처리
# 아래의 view function은 'GET/custom/{param}'에 대한 요철 처리를 담당
def custom(param):
    return param


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # 서버 run
    # 기본 설정: host:'127.0.0.1'(localhost), port=5000, debug=False