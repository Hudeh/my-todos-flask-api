from datetime import datetime
from config import db, ma, app
from werkzeug.security import generate_password_hash, check_password_hash

# create db table on start up
@app.cli.command("db_create")
def db_create():
    db.create_all()
    print("Database created")

# drop db
@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("Database dropped")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "first_name", "last_name", "username", "created_at")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    task_title = db.Column(db.String(100), nullable=False)
    task_category = db.Column(db.String(100), nullable=False)
    task_priority = db.Column(db.String(100), nullable=False)
    task_description = db.Column(db.String(500))
    start_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class TaskSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "user_id",
            "task_title",
            "task_category",
            "task_priority",
            "task_description",
            "start_date",
            "due_date",
        )


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
