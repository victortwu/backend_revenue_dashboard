import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def test_user_resource():
    return 'user controller!'

# ===== POST - register user ======

@users.route('/register', methods=['POST'])
def register():

    payload = request.get_json()

    payload['email'] = payload['email'].lower()

    payload['username'] = payload['username'].lower()

    print('From line 25:', payload)

    try:
        models.User.get(models.User.email == payload['email'])
        models.User.get(models.User.username == payload['username'])
        return jsonify(
            data={},
            message='A user already exists',
            status=401
        ), 401

    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        # pw_hash = generate_password_hash(payload['password'])

        created_user = models.User.create(
            **payload
        )

        print(created_user)

        login_user(created_user)


        created_user_dict = model_to_dict(created_user)

        print(created_user_dict)

        print(type(created_user_dict['password']))
        created_user_dict.pop('password')

        return jsonify(
            data=created_user_dict,
            message='Successfully registered user',
            status=201
        ), 201



# ======= LOGIN - POST =======
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    print('At line 65: ', payload)
    # payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()

    # look up user by email
    try:
        user = models.User.get(models.User.username == payload['username'])
        # if we got here a user with this email exists
        # check password
        user_dict = model_to_dict(user)
        #check user pw with bcrypt
        #check_password_hash: 2 args
            # the encrypted pw checking against
            # the pw attempt you are trying to verify
        password_is_good = check_password_hash(user_dict['password'], payload['password'])

        # if pw is good
        if(password_is_good):
            # log the user in
            login_user(user)

            user_dict.pop('password')

            return jsonify(
                data=user_dict,
                message='Successfully logged in' + user_dict['email'],
                status=200
            ), 200
        else:
            print('Password incorrect')

            return jsonify(
                data={},
                message="Something is not right",
                status=401
            ),401





    except models.DoesNotExist:
        #else if they don't exist
        print('username is no good')
        # respond -- bad username or password
        return jsonify(
            data={},
            message='Email or password is incorrect',
            status=401
        ), 401


# logout route
@users.route('/logout', methods=['GET'])
def logout():
    logout_user()

    return jsonify(
        data={},
        status=200,
        message='User successfully logged out'
    ), 200
