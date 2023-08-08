from flask import Blueprint

app = Blueprint("another", __name__, template_folder= 'templates')

@app.route('/another')
def another():
    return 'another'