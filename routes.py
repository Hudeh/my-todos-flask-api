# # routes.py
# from flask import request, jsonify
# from flask_jwt_extended import jwt_required,  get_jwt_identity
# from task_models import db, Task
# from app import app

# @app.route('/tasks', methods=['GET'])
# @jwt_required()
# def get_tasks():
#     current_user = get_jwt_identity()
#     tasks = Task.query.filter_by(user_id=current_user).all()
#     return jsonify([task.serialize() for task in tasks]), 200

# @app.route('/tasks/<int:id>', methods=['GET'])
# @jwt_required()
# def get_task(id):
#     task = Task.query.get(id)
#     if not task:
#         return jsonify({'message': 'Task not found'}), 404

#     return jsonify(task.serialize()), 200

# @app.route('/tasks', methods=['POST'])
# @jwt_required()
# def create_task():
#     data = request.get_json()
#     title = data.get('title')
#     description = data.get('description')
#     current_user = get_jwt_identity()

#     task = Task(title=title, description=description, user_id=current_user)
#     db.session.add(task)
#     db.session.commit()

#     return jsonify({'message': 'Task created successfully'}), 201

# @app.route('/tasks/<int:id>', methods=['PUT'])
# @jwt_required()
# def update_task(id):
#     task = Task.query.get(id)
#     if not task:
#         return jsonify({'message': 'Task not found'}), 404

#     data = request.get_json()
#     task.title = data.get('title', task.title)
#     task.description = data.get('description', task.description)
#     db.session.commit()

#     return jsonify({'message': 'Task updated successfully'}), 200

# @app.route('/tasks/<int:id>', methods=['DELETE'])
# @jwt_required()
# def delete_task(id):
#     task = Task.query.get(id)
#     if not task:
#         return jsonify({'message': 'Task not found'}), 404

#     db.session.delete(task)
#     db.session.commit()

#     return jsonify({'message': 'Task deleted successfully'}), 200
