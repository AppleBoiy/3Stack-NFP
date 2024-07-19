from datetime import datetime  # noqa

from app import db  # noqa
from app.models.token_blocklist import TokenBlocklist  # noqa
from app.models.user import User  # noqa
from flask import request
from flask_jwt_extended import (  # noqa
    create_access_token, jwt_required, current_user, get_jwt  # noqa
)  # noqa
from flask_restx import Namespace, Resource, fields  # noqa

user_ns = Namespace('users', description='User operations')

user_model = user_ns.model('User', {
    'id': fields.Integer(required=True, description='User ID'),
    'username': fields.String(required=True, description='Username'),
})


@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = User.query.all()
        return users


register_model = user_ns.model('Register', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password'),
})


@user_ns.route('/register')
class Register(Resource):
    @user_ns.doc('register_user')
    @user_ns.expect(register_model)
    def post(self):
        """Register a new user"""
        data = user_ns.payload
        username = data['username']
        password = data['password']
        if User.is_user_exist(username):
            return {'message': f"User <username:{username}> already exists"}, 400
        user = User(username=username, password=password)
        user.save()
        return {'message': f"User <username:{username}> created successfully"}, 201


login_model = user_ns.model('Login', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password'),
})


@user_ns.route('/login')
class Login(Resource):
    @user_ns.doc('login_user')
    @user_ns.expect(login_model)
    def post(self):
        """Login user"""
        data = request.json
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user)
        return {'access_token': access_token}, 200


whoami_model = user_ns.model('WhoAmI', {
    'id': fields.Integer(readOnly=True, description='The user identifier'),
    'username': fields.String(required=True, description='Username'),
})

whoami_header = user_ns.parser()
whoami_header.add_argument('Authorization', location='headers', required=True, help='Bearer <access_token>')


@user_ns.route('/whoami')
class WhoAmI(Resource):
    @user_ns.doc('whoami')
    @user_ns.expect(whoami_header)
    @user_ns.marshal_with(whoami_model)
    @jwt_required()
    def get(self):
        """Get user info"""
        return current_user


logout_header = user_ns.parser()
logout_header.add_argument('Authorization', location='headers', required=True, help='Bearer <access_token>')


@user_ns.route('/logout')
class Logout(Resource):
    @user_ns.doc('logout')
    @user_ns.expect(logout_header)
    @jwt_required()
    def post(self):
        """Logout user"""
        jti = get_jwt()["jti"]
        now = datetime.utcnow()
        db.session.add(TokenBlocklist(jti=jti, created_at=now))
        db.session.commit()
        return {"msg": "Successfully logged out"}, 200
