from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # 자동으로 '200 ok'로 처리되는 status code를 명시적으로 변경할 수 있다
    return 'hello', 204
    # 위처럼 view function은 튜플을 리턴할 수 있다

if __name__ == '__main__':
    app.run(host= "127.0.0.1", port= 5000, debug= True)