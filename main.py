from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


users = [
    {"id": 1, "name": "Ivan Petrenko", "email": "ivan@gmail.com"},
    {"id": 2, "name": "Olena Koval", "email": "olena@gmail.com"},
]

workouts = [
    {"id": 1, "user_id": 1, "type": "Cardio", "duration": 30, "date": "2024-11-12"},
    {"id": 2, "user_id": 2, "type": "Strength", "duration": 45, "date": "2024-11-11"},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Fitness API is running"})


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/workouts", methods=["GET"])
def get_workouts():
    return jsonify(workouts)

@app.route("/workouts", methods=["POST"])
def add_workout():
    data = request.get_json()
    new_workout = {
        "id": len(workouts) + 1,
        "user_id": data["user_id"],
        "type": data["type"],
        "duration": data["duration"],
        "date": data["date"],
    }
    workouts.append(new_workout)
    return jsonify(new_workout), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)