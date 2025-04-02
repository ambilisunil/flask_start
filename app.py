# register_blueprint() in Flask
# In Flask, register_blueprint() is used to modularize routes by dividing them 
# into separate Blueprints instead of defining all routes in a single file (app.py).


from flask import Flask
from routes.home import home_bp  # Import home blueprint  in routes/home.py
from routes.user import user_bp  # Import user blueprint

app = Flask(__name__)

# Register the Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(user_bp, url_prefix='/user')  # URL prefix for user routes

if __name__ == "__main__":
    app.run(debug=True)
