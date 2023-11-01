from flask_app import app
from flask_app.controllers import usersControllers
from flask_app.controllers import animeController

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
