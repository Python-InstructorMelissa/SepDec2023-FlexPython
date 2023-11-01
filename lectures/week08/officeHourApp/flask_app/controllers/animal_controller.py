from flask import redirect, render_template, request, session
from flask_app.models.animalModel import Animal
from flask_app.models.userModel import User
from flask_app import app


@app.route("/animals/new")
def new_animal():
    """Displays the create animal form."""

    root = {"title": "Parks and Animals"}

    if "user_id" not in session:
        theUser = False
    else:
        data = {"id": session["user_id"]}
        theUser = User.getOne(data)

    return render_template("/animals/new_animal.html", root=root, user=theUser)
