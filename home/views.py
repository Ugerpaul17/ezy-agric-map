from flask import Blueprint

home_vie = Blueprint('home_view', __name__)


@home_view.route('/') 
def display_home_page():
    return 'Hello, World!'