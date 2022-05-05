from flask import Flask, json, jsonify, request
app = Flask(__name__)
numbers = [1,2,3,4,5]
greeting = "greet swift"

@app.route('/',methods = ['GET'])
def hello_world():
    return jsonify({'greeting':greeting})

if __name__ == '__main__':
    app.run(debug=True)
