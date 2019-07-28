from flask import request
from View.V1.Function import LoginCheck
import os



# 게시물 보는 라우터
def showlist():
    if LoginCheck.logincheck() == False:
        return 'please login first!'

    count = 0
    data = request.form
    user = data['user']

    if os.path.exists('Data/List/'+user) == False:
        return 'there is no ' + user + '\'s list'

    DataList = ''

    for root, dirs, files in os.walk('./Data/List/'+user):

        for file in files:

            count = count + 1
            f = open('Data/List/'+user+'/'+file, 'r')
            fdata = f.readline()

            DataList = DataList + str(count) + '. '
            DataList = DataList + file + ': '
            DataList = DataList + fdata + '\n'

    return DataList