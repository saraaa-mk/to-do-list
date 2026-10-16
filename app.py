from flask import Flask 
app=Flask(__name__)
@app.route('/')
def hello():
    return "HI GUYS IM LEARNING"
@app.route('/task/<int:task_num>')
def task(task_num):
    return f"task {task_num}"
@app.post('/add')
def add_a_task():
    return "ig its working lol"
