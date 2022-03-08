from dbContext import db
from helpers import *

import logging
logger = logging.getLogger(__name__)

class Service :
    def __init__(self):
        self.service = "Service"

    def getTasks(self) :            
        try:
            query = "select * from task";
            result = db.execute(query).fetchall()
            serviceResult = { "status":"success", "message": "Tasks retrieved.","service": self.service, "method": "getTasks", "data": Helper.db_result_to_dict(result) }
            return serviceResult    
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "getTasks", "data": []}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult 

    def getTask(self, id) :
        try:
            params = { "id": id }
            query = "select * from task where id =:id";
            result = db.execute(query, params).fetchall()

            serviceResult = { "status":"success", "message": "Task retrieved.","service": self.service, "method": "getTask", "data": Helper.db_result_to_dict(result)[0] }
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "getTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult

    def addTask(self, task):
        try:
            params = task
            query = "insert into task (name, description, priority, status) values (:name, :description, :priority, :status);"
            db.execute(query, params)
            db.commit()

            serviceResult = { "status":"success", "message": "Tasks added.","service": self.service, "method": "addTask", "data": {} }
            
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "addTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult

    def updateTask(self, task):
        try:
            params = task
            query = "update task set name = :name, description = :description where id = :id;"
            db.execute(query, params)
            db.commit()

            serviceResult = { "status":"success", "message": "Tasks updated.","service": self.service, "method": "updateTask", "data": {} }
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "updateTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult

    def deleteTask(self, task):
        try:
            params = task
            query = "delete from task where id = :id;"
            db.execute(query, params)
            db.commit()

            serviceResult = { "status":"success", "message": "Tasks deleted.","service": self.service, "method": "deleteTask", "data": {} }
            return serviceResult
        except Exception as e:
            serviceResult  = { "status": "failure", "message": e.args, "service": self.service, "method": "deleteTask", "data": {}}
            logger.error(f"an exception occurred. {serviceResult}")
            return serviceResult
