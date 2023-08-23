"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, Blueprint
# from flask import Flask, request, jsonify, url_for, Blueprint
from api.utils import generate_sitemap, APIException
from api.models import db, User
import json

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {"message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"}
    return response_body, 200


@api.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        users = db.session.execute(db.select(User).order_by(User.email)).scalars()
        results = [row.serialize() for row in users]
        response_body = {'status': 'ok',
                         'message': 'I am response body: GET method',
                         "results": results}
        return response_body, 200
    if request.method == 'POST':
        request_body = request.get_json()
        user = User(email = request_body["email"],
                    password = request_body["password"],
                    name = request_body["name"],
                    phone = request_body["phone"],)
        db.session.add(user)
        db.session.commit()
        response_body = {'status': 'ok',
                         'message': 'I am response body: POST method',
                         'request_body': request_body}
        return response_body, 200


@api.route('users/<int:id>', methods=['GET','PUT', 'DELETE'])
def handle_user(id):
    if request.method == 'GET':
        user = db.get_or_404(User, id)
        print(user.serialize())
        response_body = {'status': 'ok',
                         'message': 'I am response body: GET method',
                         'user_to_return': id,
                         'results': user.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        user = db.get_or_404(User, id)
        request_body = request.get_json()
        user.email = request_body["email"]
        user.password = request_body["password"]
        user.name = request_body["name"]
        user.phone = request_body["phone"]
        db.session.commit()
        response_body = {'status': 'ok',
                         'message': 'I am response body: PUT method',
                         'user_to_modify': id,
                         'request_body': request_body}
        return response_body, 200
    if request.method == 'DELETE':
        user = db.get_or_404(User, id)
        db.session.delete(user)
        db.session.commit()
        response_body = {'status': 'ok',
                         'message': 'I am response body: PUT method',
                         'user_to_delete': id}
        return response_body, 200
