from flask_app import app
from flask_app.controllers import userController

if __name__ == "__main__":
    app.run(port=5002, debug=True)