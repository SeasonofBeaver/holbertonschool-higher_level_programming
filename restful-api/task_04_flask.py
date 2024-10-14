#!/usr/bin/python3
"""Do I need documentation here too?"""
from flask import Flask, jsonify, request, json


app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Do I need documentation here too?"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """Do I need documentation here too?"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """Do I need documentation here too?"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Do I need documentation here too?"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Do I need documentation here too?"""
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    """Do I need documentation here too?"""
    app.run(debug=True)
