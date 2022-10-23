from flask import render_template, request, redirect
from app import app, db
from app.models import Entry
import json


def dict_response_in_string_format(data):
    res = {}
    for i in data:
        res[i.id] = {"title": i.title, "content": i.description}
    return json.dumps({"reponse": str(res)})


@app.route("/")
def indexx():
    entries = Entry.query.all()
    return dict_response_in_string_format(entries)


@app.route("/index")
def index():
    entries = Entry.query.all()
    return render_template("index.html", entries=entries)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        form = request.form
        title = form.get("title")
        description = form.get("description")
        if not title or description:
            entry = Entry(title=title, description=description)
            db.session.add(entry)
            db.session.commit()
            return "ok", 200

    return "ko", 400

@app.route("/add2", methods=["POST"])
def add2():
    if request.method == "POST":
        form = request.form
        title = form.get("title")
        description = form.get("description")
        if not title or description:
            entry = Entry(title=title, description=description)
            db.session.add(entry)
            db.session.commit()
            return redirect("/")

    return "of the jedi"


@app.route("/update/<int:id>")
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template("update.html", entry=entry)

    return "of the jedi"


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            title = form.get("title")
            description = form.get("description")
            entry.title = title
            entry.description = description
            db.session.commit()
        return redirect("/")

    return "of the jedi"


@app.route("/delete/<int:id>")
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect("/")

    return "of the jedi"


@app.route("/turn/<int:id>")
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect("/")

    return "of the jedi"
