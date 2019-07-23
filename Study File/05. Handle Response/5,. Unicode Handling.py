# Flask는 텍스트를 처리할 때 유티코드를 사용한다
# 유티코드 처리를 서버에서 해주는 게 좋다
from flask import Flask, Response, jsonify
import json

app = Flask(__name__)
resp = {'key': '한글'}


@app.route('/unicode')
def unicode():
    return jsonify(resp)


@app.route('/encoded')
def encoded():
    return Response(json.dumps(resp, ensure_ascii=False), content_type='application/json; charset=utr8')

# /unicode 경우 한글이 유니코드로 처리되고, /encoded의 경우 한글이 제대로 보인다
# 아래의 경우에는 jsonify와 다르게 헤더(application/json)를 따로 설정해 줘야 한다

if __name__ == '__main__':
    app.run(debug=True)
