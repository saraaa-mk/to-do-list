from flask import Flask 
from flask import render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/task/<int:task_num>')
def task(task_num):
    return f"task {task_num}"
@app.post('/add')
def add_a_task():
    return "ig its working lol"
