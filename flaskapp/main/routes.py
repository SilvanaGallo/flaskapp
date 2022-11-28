from flask import Blueprint
from flaskapp import db
import json

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/which")
def which():
    return "API under construction"

@main.route("/check")
def check():
    result = {'status': 'OK'}
    return json.dumps(result, indent=2)