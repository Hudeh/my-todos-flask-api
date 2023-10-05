from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_restful import Api
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'task.db')

app.config["JWT_SECRET_KEY"] = "fcdr86b&qf1w&(8cb48-kw-9^44446!35xsjv#sgf!#y&42"
app.config["JWT_TOKEN_LOCATION"] = ["headers", "query_string"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_HEADER_TYPE"] = "Bearer"

# # Initialize SQLAlchemy and JWTManager (outside of the app context)
jwt = JWTManager(app)
cors = CORS(app)
db = SQLAlchemy()
api = Api(app)
ma = Marshmallow(app)
# Add CORS support
CORS(app)


