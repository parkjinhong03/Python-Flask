from flask import request
from View.V1.Function import LoginCheck
import os


# 게시물 삭제 라우터
def deletelist():
    if LoginCheck.logincheck() == False:
        return 'please login first!'

    DeleteData = request.form
    title = DeleteData['title']
    User_name = request.cookies['login']

    if os.path.exists('Data/List/'+User_name+'/'+title) == False:
        return 'this list is not exist or not your list!'
    else:
        os.remove('Data/List/'+User_name+'/'+title)
        return 'delete succeeded!'