from flask import Flask, request, make_response
import os

def logout():
    res = make_response('logout succeeded!')
    if 'login' in request.cookies:
        res.set_cookie('login', '', expires= 0)
        return res # -> Response 객체 반환 하지 않을 시 적용 X
    else:
        return 'you don\'t login!'