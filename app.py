from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data
users = {
    1: {"name": "Amit", "age": 22},
    2: {"name": "Bhumi", "age": 21}
}

# GET - View all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# GET - View one user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"message": "User not found"}), 404


# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    new_id = max(users.keys()) + 1 if users else 1

    users[new_id] = {
        "name": data["name"],
        "age": data["age"]
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[new_id]
    }), 201

@app.route('/')
def home():
    return "Welcome to the User Management REST API"

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()

    users[user_id]["name"] = data["name"]
    users[user_id]["age"] = data["age"]

    return jsonify({
        "message": "User updated successfully",
        "user": users[user_id]
    })


# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    deleted = users.pop(user_id)

    return jsonify({
        "message": "User deleted successfully",
        "user": deleted
    })


if __name__ == '__main__':
    app.run(debug=True)