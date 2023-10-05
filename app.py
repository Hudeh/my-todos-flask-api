from flask import jsonify
from config import app, jwt, db
from models import db_create
from auth_routes import user_bp
from task_routes import task_bp


# Create a URL route in our application for "/"
@app.route("/", methods=["GET"])
def index():
    return jsonify(message="Welcome to flask!")


# auth url
app.register_blueprint(user_bp, url_prefix="/api")
app.register_blueprint(task_bp, url_prefix="/api")


if __name__ == "__main__":
    with app.app_context():
        # Initialize SQLAlchemy and JWTManager within the app context
        db.init_app(app)
        jwt.init_app(app)

        # # Create the database tables
        # db_create()

    # Run the Flask app
    app.run(host="0.0.0.0", port=8000, debug=True)
