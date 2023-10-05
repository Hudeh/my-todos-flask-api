from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from models import Task, task_schema, tasks_schema
from config import db


# task route blueprint
task_bp = Blueprint(
    "task_bp", __name__, template_folder="templates", static_folder="static"
)


@task_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=current_user).all()
    return jsonify({"data": tasks_schema.dump(tasks)}), 200


@task_bp.route("/tasks/<int:id>", methods=["GET"])
@jwt_required()
def get_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    return jsonify({"data": task_schema.dump(task)}), 200


@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.get_json()
    task_title = data.get("task_title")
    task_description = data.get("task_description")
    task_category = data.get("task_category")
    task_priority = data.get("task_priority")
    start_date_str = data.get("start_date")
    due_date_str = data.get("due_date")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()

    current_user = get_jwt_identity()

    task = Task(
        task_title=task_title,
        task_description=task_description,
        task_category=task_category,
        task_priority=task_priority,
        start_date=start_date,
        due_date=due_date,
        user_id=current_user,
    )
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created successfully"}), 201


@task_bp.route("/tasks/<int:id>", methods=["PATCH"])
@jwt_required()
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()
    task.task_title = data.get("task_title", task.task_title)
    task.task_description = data.get("task_description", task.task_description)
    task.task_category = data.get("task_category", task.task_category)
    task.task_priority = data.get("task_priority", task.task_priority)
    start_date_str = data.get("start_date")
    due_date_str = data.get("due_date")
    if start_date_str and due_date_str != "":
        task.start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        task.due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    else:
        task.start_date = task.start_date
        task.due_date = task.due_date
    db.session.commit()

    return jsonify({"message": "Task updated successfully"}), 200


@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"}), 200
