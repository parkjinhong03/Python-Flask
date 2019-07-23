from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '2th server'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9055, debug= True)
    #debug -> 보편적으로 생각하는 debug 모드를 뜻함, 또한 프로젝트 내의 파일이 수정되면 자동으로 서버 restart

    # --threaded = True
    # 요청을 모두 새로운 스레드에서 처리하도록 만듬 : 직렬 처리 -> 병렬 처리