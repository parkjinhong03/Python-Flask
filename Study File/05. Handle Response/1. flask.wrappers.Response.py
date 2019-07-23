from flask import Flask, make_response, Response
# make_response() 함수 또느 Respose 클래스를 통해 response 객체를 만들 수 있다

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('Body data', 200) # -> 서버가 'Body data'값과 status code = 200을 response 해주는 객체 생성
    # 1. helper.make_response 함수를 이용한 방법

    # 헤더를 설정해 보자
    response.headers['Somethine'] = 'Value'
    # werkzueg.datastructures.Headers 클래스의 인스턴스

    return response

@app.route('/2')
def index2():
    response = Response('Hello', 200) # -> resoponse 객체를 생성하는 또 다른 방법
    # 2. wrappers.Response(werkzueg.wrappers.BaseResponse) 클래스를 이용하는 방법

    return response

if __name__ == '__main__':
    app.run(host= '127.0.0.1',port= 5000, debug= True)