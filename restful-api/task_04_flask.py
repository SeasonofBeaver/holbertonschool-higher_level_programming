#!/usr/bin/python3
"""Do I need documentation here too?"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, 
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }

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

    if not (key in data for key in ("username")):
        return jsonify({"error":"Username is required"}), 400
    if not (key in data for key in ("name")):
        return jsonify({"error":"Name is required"}), 400
    if not (key in data for key in ("age")):
        return jsonify({"error":"Age is required"}), 400
    if not (key in data for key in ("city")):
        return jsonify({"error":"City is required"}), 400

    username = data['username']
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    """Do I need documentation here too?"""
    app.run()