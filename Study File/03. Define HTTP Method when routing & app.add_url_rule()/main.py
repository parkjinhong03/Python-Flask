from flask import Flask

app = Flask(__name__)

# Flask에선 라우팅을 위한 여러 가지 방법들을 지원하고 있다.
@app.route('/')
def index():
    # 별도의 HTTP 메소드 명사가 없으면 GET 에 라우틴
    return 'GET /'


@app.route('/post-test', methods=['POST'])
# route 데코레이터에 methods 파라미터를 iterable 객체로 전달하여 다른 HTTP 메소에 대해 라우틴
# -> app.Flask.route(self, rule, **option)의 **option 에 해당
def index_post():
    # 해당 view function은 'POST /'의 요청 처리를 담당
    # POST가 아닌 메소드로 '/post-test'에 접근하면 405 Method Not Allowed 가 반환됨
    return 'POST /'


# route를 이용하여 라우팅 진행 시, 내부적으로 self.add_url_rule 메소드를 호출함
# [app.Flask]
#       def add_url_rule(self, rule, endpoint, f, **option)
app.add_url_rule('/2', 'something', lambda: 'Hello jinhong!')
# endpoint는 해당 URL rule에 대한 endpoint 이름을 말하며, app.route() 시에는 view function의 이름을 사용

if __name__ == '__main__':
    app.run()