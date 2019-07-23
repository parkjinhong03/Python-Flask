from flask import Flask, request

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def json():
    # 요청의 Content - Type이 application/json이고, 직렬하된 JSON 문자열이 들어온다면
    # request의 json property나 get_json() 메소드를 이용하면 된다
    req1 = request.json
    req1 = request.get_json()
    # 요청의 Content - Type이 application/json이 아니라면 None이 반환됨
    # json으로 설정되어있으나 아무 데이터도 전달되지 않으면 status code 400이 리턴된다

    # 요청의 타입이 json인지 확인해 주는 메소드가 있다.
    if not request.is_json:
        return 'Please set your contect type = "application/json!"', 400

    print(type(req1))
    print(req1['test_key'])
    # json 프로퍼티는 요청 테이터에 따라 파이썬 고유의 dict 또는 list 타입으로 처리된다

    return str(req1['test_key'])

if __name__ == '__main__':
    app.run(host="127.0.0.1", port= 5000, debug= True)