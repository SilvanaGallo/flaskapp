from flask import Blueprint
from flaskapp import repository
import json

items = Blueprint('items', __name__)

@items.route("/items",  methods=['GET'])
def list_items():
    return repository.list_items()


@items.route("/items",  methods=['POST'])
def create_item():
    return repository.create_item()


@items.route("/items/<int:id>",  methods=['GET'])
def get_item(id):
    return repository.get_item(id)
    

@items.route("/items/<int:id>",  methods=['PUT', 'PATCH'])
def update_item(id):
    return repository.update_item(id)
    

@items.route("/items/<int:id>",  methods=['DELETE'])
def delete_item(id):
    return repository.delete_item(id)
    