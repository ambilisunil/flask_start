from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB
db = client["task_db"]  # Database Name
tasks_collection = db["tasks"]  # Collection Name

# Home Route - Show Tasks
@app.route('/')
def index():
    tasks = list(tasks_collection.find())  # Fetch all tasks
    return render_template("todo.html", tasks=tasks)

# Add Task
@app.route('/add', methods=["POST"])
def add_task():
    title = request.form["title"]
    if title:
        tasks_collection.insert_one({"title": title})  # Insert into MongoDB
    return redirect(url_for('index'))

# Delete Task
@app.route('/delete/<task_id>')
def delete_task(task_id):
    tasks_collection.delete_one({"_id": task_id})  # Delete by ID
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
