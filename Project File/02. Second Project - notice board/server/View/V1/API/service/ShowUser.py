from View.V1.Function import LoginCheck
import os


# 사용자 명단 라우터
def showuser():
    if LoginCheck.logincheck() == False:
        return 'Please Login First!'

    count = 0
    Userlist = ''

    for root, dirs, files in os.walk('./Data/List'):
        for dir in dirs:
            count = count + 1
            Userlist = Userlist + str(count) + '. '
            Userlist = Userlist + dir + '\n'

    return 'You can choose this user\'s list:\n' + Userlist