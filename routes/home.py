from flask import Blueprint

# Define Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "Welcome to the Home Page!"
