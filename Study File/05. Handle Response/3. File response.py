from flask import Flask, request
from flask import send_from_directory, send_file
# flask.helpers 패키지의 send_from_directory나 send_file함수를 이용해 파일을 전송할 수 있다
import os.path

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    file_name = request.args['name']
    if os.path.isfile('./img/'+file_name):
        return send_from_directory('./img', file_name)
        # -> 만약 내 local에 파일이 존재하면 그 파일을 response 해줘라.
    else:
        return "file does not exist!"
        # -> 파일이 존재하지 않으면 이 와 같은 문구 반환


    # path를 safe_join하고, 파일의 full path를 가져와 send_file로 제어를 넘기는 형태이다

if __name__ == '__main__':
    app.run(host= "127.0.0.1", port= 5000, debug= True)

