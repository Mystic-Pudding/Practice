from flask import Flask
import random
import functions
import pageFromAnotherFile

app = Flask(__name__)
app.register_blueprint(pageFromAnotherFile.app)

@app.route('/')
def mainPage() -> str:
    return str(random.random())

@app.route('/create/<id>')
def create(id) -> str:
    functions.hellofunc()
    fetcher = functions.returnhello()
    print(fetcher)
    fetcher = functions.receiveHello(text= str(id))
    print(fetcher)
    return "Create" + id

app.run(port= 8000, debug= True)