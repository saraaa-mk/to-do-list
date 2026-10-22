from flask import Flask
from flask import render_template
app=Flask(__name__)
tasks=[{"id":1, "text": "Solve math tools for crypto", "done": False, "pinned": True }, {"id":2, "text": "Clean ur closet", "done": True, "pinned": False }]
@app.route('/')
def hello():
    return render_template("index.html", task=tasks)
@app.route('/task/<int:task_num>')
def task(task_num):
    return f"task {task_num}"
@app.post('/add')
def add_a_task():
    return "ig its working lol"
