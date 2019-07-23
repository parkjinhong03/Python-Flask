from flask import Flask, abort


app = Flask(__name__)


@app.route('/')
def index():
    abort(400)
    #   def abort(status, *args, **kwargs)
    # abort() 함수는 HTTP 예외 코드 (400번대 이상의 상태 코드)를 리턴해 주는 역할을 한다

if __name__ == '__main__':
    app.run(debug=True)