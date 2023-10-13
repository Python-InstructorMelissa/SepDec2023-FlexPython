# Starting a Flask app

## Application/Folder Structure As of Week 7
- server.py
- flask_app/
    - __init__.py
    - templates/
        - index.html
    - static/
        - css/
            - style.css
        - js/
            - script.js
        - images/
            - logo.jpg
    - controllers
        - controllerFile.py

## Create Environment
- At root of folder
- Install packages

```
python -m pipenv install flask

```
- Start the environment
```
python -m pipenv shell

```
## Start adding code to files
### __init__.py
```python
from flask import Flask

app = Flask(__name__)


app.secret_key = "DreBrunoKeithCoreyLydia"
```

### server.py
```python
from flask_app import app
# list each route file here


if __name__ == "__main__":
    app.run(debug=True)
```