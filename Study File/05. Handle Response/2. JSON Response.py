from flask import Flask, json

app = Flask(__name__)


@app.route('/')
def json():
    # JSON Object와 Python Dictionary, JSON Array와 Python List가 서로 대응된다

    data = [{'name': 'planb', 'age': 18}, {'name': 'jgc', 'age': 18}] # -> list type

    # 하지만 아래의 단순한 구문은 response에 성공하지 않는다
    # > return dataor: 'list' object is not ca
    #     # TypeErrllable
    # JSON 데이터를 직렬화해 주어야 한다


    # json response를 위한 대표적인 3가지 방법!
    # 1. return str(data)
    # 2. return json.dumps(data)
    # 위 두 경우는 Content Type이 text/html이기 때문에 따로 헤더를 적용해줘야 한다

    # flask의 jsonify는 Content Type이 application/json으로 설정되고, 반환 데이터도 잘 직렬화되어 처리된다
    from flask  import jsonify

    return jsonify(data) # -> data 값을 json 형식으로 잘 정리해서 반환해준다

if __name__ == '__main__':
    app.run(host= "127.0.0.1", port= 5000, debug= True)