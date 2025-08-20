from flask import Flask, request, jsonify
import task_service

app = Flask(__name__)

@app.route("/tasks", methods=["POST"])
def create_task():
 data = request.get_json() or {}
 title = data.get("title")
 if not title:
    return jsonify({"error": "title required"}), 400
 task = task_service.create_task(title, data.get("description"))
 return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def list_tasks():
  return jsonify(task_service.list_tasks())

if __name__ == "__main__":
   app.run(debug=True)
