from os import sendfile
from flask import Flask
from flask import request
from flask import send_file
app = Flask(__name__)

@app.route("/")
def hello():
    filename=request.args.get('image')    #2번째 파라미터는 디폴트값.    #flask url request http://127.0.0.1:5000/?image=b1.png이런식으로 사용.
    return send_file(filename,
                     mimetype='image.png',
                     attachment_filename='b1.png',# 다운받아지는 파일 이름. 
                     as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)
