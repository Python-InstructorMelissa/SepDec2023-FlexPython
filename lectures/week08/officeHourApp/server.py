from flask_app import app
from flask_app.controllers import routes
from flask_app.controllers import animal_controller
from flask_app.controllers import parkController
from flask_app.controllers import userController


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
