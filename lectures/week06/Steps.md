# Creating new Assignment / Project

1. Create a Project Folder
2. Create server.py
3. Create & start virtual environment
    a. Windows
        - pipenv install flask (python -m pipenv install flask)
        - pipenv shell (python -m pipenv shell)
    b. Mac
        - pipenv install flask (python3 -m pipenv install flask)
        - pipenv shell (python3 -m pipenv shell)
4. Fill out server.py with at least the following
    ```python
    from flask import Flask
    app = Flask(__name__)


    if __name__=="__main__":
        app.run(debug=True)
    ```
5. Create 1st route
    ```python
        @app.route('/')
        def index():
            #code here
            return
    ```
6. Start Server
    - in terminal python server.py (python3 server.py)
    - ctrl + click 127.0.0.1:5000 (127.0.0.1:5001)
7. Finish work continue to test
8. ctrl + c (exit the server)
9. exit (to close environment)