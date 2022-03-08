from flask import request
from flask_restful import Resource

from service import Service

class TaskList(Resource):
    def get(self):
        svc = Service()
        return svc.getTasks()

    def post(self): #resource add
        svc = Service()
        return svc.addTask(request.get_json()), 201 

class Task(Resource):
    def get(self, id):
        svc = Service()
        return svc.getTask(id)

    def delete(self, id): 
        svc = Service()
        return svc.deleteTask(request.get_json()), 204

    def put(self, id): #resource update
        svc = Service()
        return svc.updateTask(request.get_json()), 201