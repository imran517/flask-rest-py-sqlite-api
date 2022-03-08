from flask import Flask
from config import config
from flask_restful import Api
from controller import *


app = Flask(__name__)
api = Api(app)

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<id>')

if __name__ == '__main__':
    app.run(debug=True, port=config.api.port())