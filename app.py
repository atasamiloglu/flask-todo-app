from flask import Flask, render_template, request, redirect, url_for
from config import Config
from extensions import db, login_manager
from models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == "POST":

        title = request.form["title"]

        new_task = Task(
            title=title,
            user_id=current_user.id
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("index"))

    tasks = Task.query.filter_by(user_id=current_user.id).all()

    return render_template("index.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if not user:
            return "User not found!"

        if not check_password_hash(user.password, password):
            return "Incorrect password!"

        login_user(user)
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match!"

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            return "Username or email already exists!"

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/complete/<int:task_id>")
@login_required
def complete_task(task_id):

    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        return "Unauthorized", 403

    task.completed = True

    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        return "Unauthorized", 403

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("index"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)