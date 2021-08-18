from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

"""
~ Author = Faroxx
~ Git = https://github.com/Fdemiroz/server
https://www.youtube.com/watch?v=GMppyAPbLYk
"""
app = Flask(__name__)
api = Api(app)

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("user_name", type=str, help="*required -> fill in username", required=True)
user_put_args.add_argument("e-mail", type=str, help="*required -> fill in e-mail", required=True)
user_put_args.add_argument("password", type=str, help="*required -> fill in password", required=True)

users = {}

def abort_if_no_user_id(user_id):
	if user_id not in users:
		abort(404, message=f'user with id {user_id} not found..')

def abort_if_user_exists(user_id):
	if user_id in users:
		abort(409, message=f'user {user_id} already exists..')

class User(Resource):
	def get(self, user_id):
		abort_if_no_user_id(user_id)
		return users[user_id]

	def put(self, user_id):
		abort_if_user_exists(user_id)
		args = user_put_args.parse_args()
		users[user_id] = args
		return users[user_id], 201

	def delete(self, user_id):
		abort_if_no_user_id(user_id)
		del users[user_id]
		return '', 204

api.add_resource(User, "/user/<int:user_id>")


if __name__ == "__main__":
	app.run(debug=True)
