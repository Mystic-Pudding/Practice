from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1 : {
        "task" : "Write hello",
        "summary" : "write ..."
        },
    2 : {
        "task" : "Write hello2",
        "summary2" : "write ...2"
    },
    3 : {
        "task" : "Write hello",
        "summary3" : "write ...3"
    }
}

postArgs = reqparse.RequestParser()
postArgs.add_argument("task", type= str, help= "Task is required", required= True)
postArgs.add_argument("summary", type= str, help= "Summary is need", required= True)


class TodoList(Resource):
    def get(self):
        return todos

class Todo(Resource):
    def get(self, todoId):
        return todos[todoId]
    
    def post(self, todoId):
        args = postArgs.parse_args()
        if todoId in todos:
            abort(409, "Task Id already taken")
        todos[todoId] = {"task" : args["task"], "summary" : args["summary"]}
        return args

api.add_resource(Todo, '/todos/<int:todoId>')
api.add_resource(TodoList, '/todos')



























# class HelloWorld(Resource):
#     def get(self):
#         return {'data' : 'Hello, world'}
    
# class HelloName(Resource):
#     def get(self, name):
#         return {'data':'hello ' + name}



# api.add_resource(HelloWorld, '/helloworld')
# api.add_resource(HelloName, '/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug= True)