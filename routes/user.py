from flask import Blueprint

user_bp = Blueprint('user', __name__)

# @user_bp.route('/user/<name>')
@user_bp.route('/<name>')  # if we add /user route will like /user/user

def user_profile(name):
    return f"Hello, {name}! This is your profile."
