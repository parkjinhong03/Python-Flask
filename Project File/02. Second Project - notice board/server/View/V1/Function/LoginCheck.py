from flask import request

# 쿠키를 이용해서 로그인이 되어 있는지를 확인하는 함수
def logincheck():
    if 'login' in request.cookies:
        return True
    else:
        return False