from flask_app import app
# list each route file here
from flask_app.controllers import routes


if __name__ == "__main__":
    app.run(debug=True)