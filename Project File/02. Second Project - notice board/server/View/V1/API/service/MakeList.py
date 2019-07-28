from flask import request
from View.V1.Function import LoginCheck
import os

# 게시물 등록 라우터
def makelist():
    if request.method == 'POST':
        ListData = request.form
        title = ListData['title']
        description = ListData['description']

        if LoginCheck.logincheck() == False:
            return 'please login first!'

        User_Name = request.cookies['login']

        if os.path.isdir('Data/List/'+User_Name) == False:
            os.makedirs(os.path.join('List/'+User_Name))

        if os.path.exists('Data/List/'+User_Name+'/'+title) == True:
            return 'this title list is exists!'
        else:
            f = open('Data/List/'+User_Name+'/'+title, 'w')
            f.write(description)

            return 'make list succeeded!'