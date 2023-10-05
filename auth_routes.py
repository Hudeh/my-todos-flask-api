from flask import request, jsonify,Blueprint
from flask_jwt_extended import create_access_token
from config import db, app
from models import User,user_schema

# user route blueprint
user_bp = Blueprint(
    'user_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

# signup route
@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not username or not password:
        return jsonify({'message': 'Both username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    user = User(username=username,first_name=first_name,last_name=last_name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'status':True, 'message': 'User created successfully'}), 201

# login route
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'message': 'Login success','user':user_schema.dump(user), 'access_token': access_token}), 200
