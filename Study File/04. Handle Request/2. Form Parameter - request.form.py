from flask import Flask, request

app = Flask(__name__)
# HTTP의 POST 메소드는 서버에게 '리소스를 작성'하라는 의미로 사용.

@app.route('/', methods=['POST'])
def index():
    return request.form['test_key']
    # form도 args와 동일하게 MultiDict 객체다


if __name__ == '__main__':
    app.run(host= "127.0.0.1", port= 5000, debug=True)