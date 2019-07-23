from flask import Flask, Blueprint

blueprint1 = Blueprint('test1', __name__) # -> 첫 번째 Blueprint인 blueprint1 객체 선언


@blueprint1.route('/hello') # -> blueprint1에서 /hello url 라우팅
def hello():
    return 'hello'


@blueprint1.route('/hi') # -> blueprint1에서의 /hi url 라우팅
def hi():
    return 'hi'


blueprint2 = Blueprint('test2', __name__) # -> 두 번째 Blueprint인 blueprint2 객체 선언


@blueprint2.route('/ok') # -> blueprint2에서의 /ok url 라우팅
def ok():
    return 'ok'


@blueprint2.route('/bye') # -> blueprint2에서의 /bye url 라우팅
def bye():
    return 'bye'


app = Flask(__name__) # -> Flask 객체 선언

app.register_blueprint(blueprint1, url_prefix='/test1') # -> Flask 객체에 blueprint1등록 후 url_prefix를 '/test1'로 설정
app.register_blueprint(blueprint2, url_prefix='/test2') # -> Flask 객체에 blueprint2등록 후 url_prefix를 '/test2'로 설정


@app.errorhandler(404)
def error(e):
    return 'wrong URL!'


@app.route('/')
def index():
    return 'use Blueprint!'

if __name__ == '__main__':
    app.run(debug=True)