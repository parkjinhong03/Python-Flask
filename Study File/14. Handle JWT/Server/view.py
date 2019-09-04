from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request


# ID를 주고 JWT token을 받을 수 있는 view function
def get():
    data = request.json
    _userID = data['id']

    # create_access_token 함수를 이용하여 flask에서 잘 돌아갈 수 있는 토큰을 발급해준다.
    access_token = create_access_token(identity=_userID)

    return {"access_token": access_token, "code": 200}, 200


# JWT token을 주고 그 Token이 가지고 있는 데이터를 반환해주는 view function
@jwt_required # -> 이 데코레이터를 추가하면 Header에 Authorization 값으로 JWT Token을 주지 않으면, 엑세스 거부를 일으켜 준다.
def send():
    # Authorization 값으로 받은 JWT Token을 자동으로 파싱해주어 그 Token이 가지고 있는 데이터를 반환해주는 함수를 이용해서 ID 값을 알아낼 수 있다.
    _id = get_jwt_identity()

    return {"id": _id, "code": 200}, 200