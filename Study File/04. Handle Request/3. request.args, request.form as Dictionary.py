from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # 원래 우리가 요청 데이터에 접근하게 사용했던 방법은 아래와 같았다
    print(request.args['test_key'])

    # 만약 value를 int형으로 받아야 한다면, 아래처럼 캐스팅을 해야할 것이다
    value = int(request.args['test_key'])
    print(value)


    value = request.args.get('test_key', type=int)
    # request값을 받아오는 또 다른 방법으로 첫 번째 인자값에 요청 데이터의 Name
    # ( -> .../?a=3 에서 a)의 값을 적는다
    # get('test_key2')만 쓸수도 있다
    # 위처럼 기본값 처리와 캐스팅에 도움을 받기 위해 get()을 사용하곤 한다

    print(value)
    print(type(value))

    return ''

if __name__ == '__main__':
    app.run(host="127.0.0.1", port= 5000, debug = True)