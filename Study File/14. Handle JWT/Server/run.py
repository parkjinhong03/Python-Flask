from flask_jwt_extended import JWTManager
from flask import Flask
import view # view function이 정리되어있는 view.py 파일 임포트


app = Flask(__name__)

# 보완 강화를 위해 app.config애 JWT_SECRET_KEY를 추가한다.
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
# jwt를 사용하기 위한 JWTmanager를 이용한 기본 설정.
jwt = JWTManager(app)

app.add_url_rule('/get-jwt', 'get', view.get)
app.add_url_rule('/send-jwt', 'send', view.send)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)