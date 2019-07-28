from flask import Flask

from View.V1.API.auth import LogOut, LogIn, SignUp
from View.V1.API.service import ShowUser, ShowList, DeleteList, MakeList

app = Flask(__name__)


app.add_url_rule('/login', 'login', LogIn.login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', LogOut.logout, methods=['POST'])
app.add_url_rule('/signup', 'signup', SignUp.signup, methods=['GET', 'POST'])
app.add_url_rule('/makelist', 'makelist', MakeList.makelist, methods=['GET', 'POST'])
app.add_url_rule('/deletelist', 'deletelist', DeleteList.deletelist, methods=['POST'])
app.add_url_rule('/showuser', 'showuser', ShowUser.showuser, methods=['POST'])
app.add_url_rule('/showlist', 'showlist', ShowList.showlist, methods=['POST'])


if __name__ == '__main__':
    app.run(debug= True, host="10.156.147.138", port= 5000)