from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from todo import db
from todo.models import Task


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        tasks = []
        tasks = Task.query.filter_by(author=current_user).order_by(Task.position)
        return render_template("home.html", title="Home", tasks=tasks)
    else:
        return redirect(url_for("main.about"))


@main.route("/about")
def about():
    return render_template("about.html", title="About")


@main.route("/task/create", methods=["POST"])
@login_required
def create_task():
    task = Task(description=request.form["desc"], user_id=request.form["id"])
    db.session.add(task)
    db.session.commit()
    tasks = Task.query.filter_by(author=current_user).order_by(Task.position)
    return render_template("create_task.html", tasks=tasks)


@main.route("/task/delete", methods=["POST"])
@login_required
def delete_task():
    task = Task.query.filter_by(id=request.form["id"]).first()
    db.session.delete(task)
    db.session.commit()
    return {"result": "success"}


@main.route("/task/edit", methods=["POST"])
@login_required
def edit_task():
    task = Task.query.filter_by(id=request.form["id"]).first()
    task.description = request.form["desc"]
    db.session.commit()
    return {"result": "success"}


@main.route("/task/sort", methods=["POST"])
@login_required
def sort_tasklist():
    task = Task.query.filter_by(id=request.form["id"]).first()
    task.position = request.form["pos"]
    db.session.commit()
    return {"result": "success"}


""" @main.route("/reset_db")
def rdb():
    db.drop_all()
    db.create_all()
    return {"result": "success"} """
