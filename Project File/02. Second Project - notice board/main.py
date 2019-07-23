from flask import Flask, request, make_response, Response
import os


# 쿠키를 이용해서 로그인이 되어 있는지를 확인하는 함수
def LoginCheck():
    if 'login' in request.cookies:
        return True
    else:
        return False


app = Flask(__name__)


# 로그인 라우터
@app.route('/login', methods=['POST', 'GET'])
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


# 로그아웃 라우터
@app.route('/logout', methods=['POST'])
def Logout():
    res = make_response('logout succeeded!')
    if 'login' in request.cookies:
        res.set_cookie('login', '', expires= 0)
        return res # -> Response 객체 반환 하지 않을 시 적용 X
    else:
        return 'you don\'t login!'


# 회원가입 라우터
@app.route('/signup', methods=['POST', 'GET'])
def Signup():
    if request.method == 'POST':
        SignupData = request.form
        id = SignupData['id']
        pw = SignupData['pw']
        if os.path.exists('User/'+id) == True:
            return 'already exist id!'
        else:
            f = open('User/' + id, 'w')
            f.write(pw)

            return 'good!!'


# 게시물 등록 라우터
@app.route('/makelist', methods=['POST', 'GET'])
def Makelist():
    if request.method == 'POST':
        ListData = request.form
        title = ListData['title']
        description = ListData['description']

        if LoginCheck() == False:
            return 'please login first!'

        User_Name = request.cookies['login']

        if os.path.isdir('List/'+User_Name) == False:
            os.makedirs(os.path.join('List/'+User_Name))

        if os.path.exists('List/'+User_Name+'/'+title) == True:
            return 'this title list is exists!'
        else:
            f = open('List/'+User_Name+'/'+title, 'w')
            f.write(description)

            return 'make list succeeded!'


# 게시물 삭제 라우터
@app.route('/deletelist', methods=['POST'])
def Deletelist():
    if LoginCheck() == False:
        return 'please login first!'

    DeleteData = request.form
    title = DeleteData['title']
    User_name = request.cookies['login']

    if os.path.exists('List/'+User_name+'/'+title) == False:
        return 'this list is not exist or not your list!'
    else:
        os.remove('List/'+User_name+'/'+title)
        return 'delete succeeded!'


# 사용자 명단 라우터
@app.route('/showuser', methods=['POST'])
def Showuser():
    count = 0
    Userlist = ''

    if LoginCheck() == False:
        return 'please login first!'

    for root, dirs, files in os.walk('./List'):
        for dir in dirs:
            count = count + 1
            Userlist = Userlist + str(count)+'. '
            Userlist = Userlist + dir + '\n'

    return 'You can choose this user\'s list:\n' + Userlist


# 게시물 보는 라우터
@app.route('/showlist', methods=['POST'])
def Showlist():
    if LoginCheck() == False:
        return 'please login first!'

    count = 0
    data = request.form
    user = data['user']

    if os.path.exists('List/'+user) == False:
        return 'there is no ' + user + '\'s list'

    DataList = ''

    for root, dirs, files in os.walk('./List/'+user):

        for file in files:

            count = count + 1
            f = open('List/'+user+'/'+file, 'r')
            fdata = f.readline()

            DataList = DataList + str(count) + '. '
            DataList = DataList + file + ': '
            DataList = DataList + fdata + '\n'

    return DataList


if __name__ == '__main__':
    app.run(debug= True)

