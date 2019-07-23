from flask import Flask, abort

app = Flask(__name__)


@app.errorhandler(404)
#   def errorhandler(self, code_or_exception)
# 서버에서 반환하는 HTTP 예외 코드 (400번대 이상)의 exception을 관리할 수 있다
# ex) 모든 404 not found 에 대해 다른 페이지를 리턴한다.
def error(e):
    # 서버가 404를 반환하려 한다면, 해당 함수가 호출된다
    print(type(e))
    print(e) # -> 매게변수로 받은 에러 변수 e의 종로와 값 출력
    return 'hello'


@app.route('/') # -> / 경로로 들어올 경우 404 status code return
def test():
    abort(404)

@app.errorhandler(AssertionError)
# view function에서 발생하는 AssertionError를 intercept하여 처리
def assertion_error(e):
    print(e)
    return 'AssertionError :(', 500


@app.route('/2')
def test2():
    raise AssertionError()

# view function에서 400, 500번대 status code 반환 시, 내부적으로 'HTTPException'이 발생하는 것임
# 따라서 errorhandler를 'Exception'에 대해 크게 잡는 경우 인스턴스를 체크하여 HTTPException인 경우 그에 맞는 status code를 response하는 것이 좋다

if __name__ == '__main__':
    app.run(debug=True)