from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm, LoginForm, TaskForm
from app.models import User, Task
from . import db
from flask_login import login_user, login_required, logout_user, current_user

main = Blueprint('main', __name__)


@main.route("/")
def index():
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        form = TaskForm()
        return render_template("index.html", tasks=tasks, form=form)
    return redirect(url_for("main.login"))


@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already exists.", "error")
            return redirect(url_for("main.register"))

        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login successful.", "success")
            return redirect(url_for("main.index"))
        flash("Invalid username or password.", "error")

    return render_template("login.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.login"))


@main.route("/add", methods=["POST"])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(content=form.content.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        flash("Task added.", "success")
    else:
        flash("Failed to add task. Please try again.", "error")

    return redirect(url_for("main.index"))


@main.route("/update/<int:task_id>")
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        flash("Unauthorized access.", "error")
        return redirect(url_for("main.index"))

    task.is_done = not task.is_done
    db.session.commit()
    flash("Task updated.", "success")
    return redirect(url_for("main.index"))


@main.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        flash("Unauthorized access.", "error")
        return redirect(url_for("main.index"))

    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "success")
    return redirect(url_for("main.index"))
