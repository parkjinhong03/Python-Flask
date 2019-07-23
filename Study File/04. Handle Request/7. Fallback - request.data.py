import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    # request.data는 Flask가 처리하지 못하는 type 요청이 오더라도 요청 데이터를 문자열 형태로 가져온다
    # request.data는 fallback(어떤 조건에도 일치하지 않아 적합한 처리 요소가 선택되지 않아 적합한 처리 요소가 선택되지 못한 경우 선택하는 기본 처리기)
    # 으로 사용되기 때문에 대체적으로 비어 있다

    req = json.loads(request.data)

    return str(req['test_key'])

if __name__ == '__main__':
    app.run(debug= True)