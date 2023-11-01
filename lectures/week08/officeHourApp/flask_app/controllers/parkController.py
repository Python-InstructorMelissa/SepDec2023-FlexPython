from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.parkModel import Park
from flask_app.models.userModel import User

# root = {
#     'title': 'title'
# }


@app.route("/parks")
def allParks():
    root = {"title": "Parks and Animals"}
    # print('the session', session['user_id'])
    if "user_id" not in session:
        theUser = False
    else:
        data = {"id": session["user_id"]}
        theUser = User.getOne(data)
    theParks = Park.getAll()
    return render_template("index.html", parks=theParks, root=root, user=theUser)


@app.route("/parks/new")
def new_park():
    """Displays the create park form."""

    root = {"title": "Parks and Animals - Create a Park"}
    if "user_id" not in session:
        theUser = False
    else:
        data = {"id": session["user_id"]}
        theUser = User.getOne(data)
    return render_template("/parks/new_park.html", root=root, user=theUser)


@app.route("/parks/create", methods={"POST"})
def create_park():
    """Creates a new park."""

    Park.save(request.form)
    return redirect("/parks")


@app.route("/parks/<int:park_id>")
def view_park(park_id):
    """Displays the details of one park."""

    root = {"title": "Parks and Animals - Park Details"}
    if "user_id" not in session:
        theUser = False
    else:
        data = {"id": session["user_id"]}
        theUser = User.getOne(data)

    park_data = {"id": park_id}

    park = Park.getOne(park_data)

    return render_template("/parks/view_park.html", root=root, user=theUser, park=park)
