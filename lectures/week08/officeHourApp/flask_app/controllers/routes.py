from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.parkAnimals import park
from flask_app.models.userModel import User

# ================================================
# These are hard coded routes no database
# ================================================

# ! You can use the better comments extension to color your comments

# ********** This is another version **********

# root = {
#     'title': 'title'
# }


@app.route("/")
def redirect_to_all_parks():
    """Redirect the user from root route to /parks."""

    return redirect("/parks")


@app.route("/fakeData")
def index():
    theData = park
    root = {"title": "Hard Coded Data"}
    print("what does my data look like", theData)
    if "user_id" not in session:
        theUser = False
    else:
        data = {"id": session["user_id"]}
        theUser = User.getOne(data)
    return render_template("fakeData.html", data=theData, root=root, user=theUser)
