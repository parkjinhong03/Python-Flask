from flask import Flask, abort
# 커스텀 HTTPException을 만들어 보자

from werkzeug.exceptions import HTTPException, default_exceptions, Aborter, _aborter
from werkzeug.http import HTTP_STATUS_CODES


class Payme(HTTPException):
    # HTTPException 클래스를 상속받아 클래스를 하나 만든다

    code = 500
    # code 필드는 필수

    description = 'I am sorry'
    # description 필드는 옵션이다. Status message에 보내지는 게 아니라, <p> 태그에 들어가는 설명이다

default_exceptions[Payme.code] = Payme # -> ????
#  기본 exception에 직접 만든 오류 코드를 심는다

HTTP_STATUS_CODES[Payme.code] = Payme.description # -> (web title과 text가 Payme.status_code & Payme.description 값으로 뜸)
#  이건 status message를 관리하기 위해 사용한다

_aborter = Aborter() # -> ????

app = Flask(__name__)

@app.route('/')
def index():
    abort(Payme.code) # -> Payme.code 값으로 status_code가 뜨도록 함


if __name__ == '__main__':
    app.run(debug=True)