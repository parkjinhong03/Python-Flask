from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/upload')
def load_file():
    return render_template('upload.html')
    # templates 디렉토리에 저장되어 있는 html 코드 랜더 해오기


@app.route('/uploader', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # request.files를 이용해 multipart/form-data로 전달되는 파일에 접근할 수 있다
        f = request.files['file'] # -> 'file'은 html의 input 태그에서 form 으로 넘겨주는 값의 name 값이다.
        # 디렉토리가 존재하지 않으면 오류가 발생한다
        f.save('uploads/'+f.filename) # -> uploads 라는 디렉토리에 customer의 filename의 이름으로 local 저장소에 저장한다

    return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port= 5000, debug= True)