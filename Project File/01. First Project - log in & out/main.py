from flask import  Flask, request, render_template, jsonify
import os
app = Flask(__name__)


@app.route('/login')
def login_html():
    return render_template('login.html')


@app.route('/login_process', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.form

        if os.path.exists("UserData/"+data['id']) == True:
            f = open('UserData/'+data['id'], 'r')
            pw = f.readline()

            if data['pw'] == pw:
                return 'login successful!'

            elif data['pw'] != pw:
                return 'wrong password!'

        else:
            return 'wrong id!'

@app.route('/signup')
def sign_html():
    return render_template('signup.html')


@app.route('/signup_process', methods=['POST', 'GET'])
def sign():
    if request.method == 'POST':
        data = request.form

        f = open("UserData/"+data['id'], 'w')
        f.write(data['pw'])

        return 'signup successful!'

if __name__ == '__main__':
    app.run(host= "127.0.0.1", port= 5000, debug= True)