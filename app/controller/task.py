from werkzeug.exceptions import HTTPException
from flask import jsonify, request
from app import ma
from app.model.Task import Task

class TaskSchema(ma.Schema):
    name = ma.Str(required=True)
    status = ma.Int()
    id = ma.Int()

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

def init_app(app):
    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.find_all()
        return {"result" : tasks_schema.dump(tasks)}


    @app.route('/task', methods=['POST'])
    def create_task():
        result = task_schema.load(request.json)

        task = Task(result['name'], 0)
        Task.create(task)

        return {"result": task_schema.dump(task)}, 201

    @app.route('/task/<string:id>', methods=['PUT'])
    def update_task(id):
        result = task_schema.load(request.json)
        task = Task.find_one(id)
        task.name = result['name']
        task.status = result['status']
        Task.update(task)
        return task_schema.dump(task)


    @app.route('/task/<string:id>', methods=['DELETE'])
    def delete_task(id):
        task = Task.find_one(id)

        if task is None:
            return {"result" : "can't find task"}

        Task.delete(task)
        return {}


    @app.errorhandler(Exception)
    def internal_error(e):
        code = 500
        print(e)
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=code, text=str(e)), code