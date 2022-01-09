from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route("/")

def hello():    #flask url request http://127.0.0.1:5000/?name=hello&old=15 이런식으로 사용.
    temp=request.args.get('name','default')
    temp2=request.args.get('old',str(13))
    name_array = [temp,"name"]
    length =  len(name_array)
    return jsonify(name=name_array,old=temp2,length=length)   #temp=[temp,temp2] 이런식으로 리스트 형태로 보내는것도 가능

if __name__ == '__main__':
    app.run(debug=True)
