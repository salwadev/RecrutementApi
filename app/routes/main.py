from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello, World!"  # Ou toute autre route que tu souhaites définir
