from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello Class Whats happening!'  # Return the string 'Hello World!' as a response

# @app.route('/new')
# def newRoute():
#     return "New route"

# # Here the second parameter is cast into an integer before being passed to the function
# @app.route('/hello/<name>/<int:num>') 
# def hello(name, num):
#     return f"Hello, {name * num}"



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.

