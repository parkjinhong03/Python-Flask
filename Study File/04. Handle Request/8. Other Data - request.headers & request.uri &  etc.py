from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    # request 객체에는 아직 배우지 못한 수 많은 속성들이 존재한다

    print(request.host, request.remote_addr)
    # request.host -> 현재 서버가 열린 HTTP의 host 값과 port값 반환
    # request.remote_addr -> 단지 host 값만 반환

    print(request.method, request.url)
    # request.method -> 현재 http에서 통신되고 있는 method 반환
    # request.url -> 서버가 열린 주소 즉, url 값 반횐

    print(request.headers) # -> HTTP 헤더에 대한 정보 반환
    print(request.is_xhr) # -> 무슨 기능인지 잘 모르겠음

    return 'hello'

if __name__ == '__main__':
    app.run(host= "127.0.0.1", port= 5000, debug= True)