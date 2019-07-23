from flask import Flask

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
print(app.logger) # -> 기본 설정이 WARNING이므로 WARNING 출력
# Flask.logger는 'flask.app'이라는 이름의 logger를 반환
# 여기에 custom logger를 붙여줄 수 있다

def make_logger():
    handler = RotatingFileHandler('server_log.log', maxBytes=100000, backupCount=5) # -> log 기록을 file에 저장하기 위해 클래스 선언
    # 1. RotatingFileHandler 클래스를 통해 handler 객체를 얻고

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s") # -> log file에 acstime, levelname, message가 순서되로 기록된다
    # 2. loggin.Formatter를 사용하야 로그 포매팅

    handler.setFormatter(formatter) # -> 위에서 Formatter 설정한 것을 핸들러에 설정한다
    # 3, 핸들러에 setFormatter

    app.logger.addHandler(handler) # -> 실제로 app.logger에 핸들러를 추가한다
    # 4. app의 logger property에 핸들러 추가

    app.logger.setLevel(logging.INFO) # -> logger의 level을 info로 설정한다
    # 5. logger의 level을 세팅(어떤 단계 이상의 로그를 기록할지)
    # -> 기본 level은 WARNING

make_logger()

print(app.logger) # -> 따로 level을 설정 해 주었으므로 info가 출력된다

app.logger.info('----- Logger started -----') # -> logging이 시작되면 INFO level로 log 파일에 저장


@app.route('/')
def index():
    app.logger.info('Access index!') # -> 클라이언트가  / 경로로 요청을 하면 log에 info 레벨로 Access index! 값을 저장시킨다.
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)