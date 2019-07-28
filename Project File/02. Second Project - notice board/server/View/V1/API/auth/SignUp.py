from flask import Flask, request
import os


def signup():
    if request.method == 'POST':
        SignupData = request.form
        id = SignupData['id']
        pw = SignupData['pw']
        if os.path.exists('Data/User/'+id) == True:
            return 'already exist id!'
        else:
            f = open('Data/User/' + id, 'w')
            f.write(pw)

            return 'good!!'