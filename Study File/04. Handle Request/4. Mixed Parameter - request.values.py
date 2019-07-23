from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    # args와 form은 request.values 객체에 섞여 있따
    print(type(request.values))
    # print(request.values)
    print(request.values['query-param'])
    print(request.values['form-param'])
    # request.values['key'] -> key에 해당되는 value 값을 출력해줌

    return 'hello'

if __name__ == '__main__':
    app.run(host= '127.0.0.1', port= 5000, debug= True)