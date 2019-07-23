from flask import Flask, request, make_response, Response
import os

def Login():
    if request.method == 'POST':
        LoginData = request.form
        id = LoginData['id']
        pw = LoginData['pw']

        if 'login' in request.cookies:
            return 'you alreay login!'

        if os.path.exists("User/"+id) == True:
            f = open('User/'+id, 'r')
            real_pw = f.readline()

            if pw == real_pw:
                res = make_response('login succeeded!')
                res.set_cookie('login', id)

                return res
            elif not pw == real_pw:
                return 'wrong password!'

        else:
            return 'wrong id!'