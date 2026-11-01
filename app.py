from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
app=Flask(__name__)
tasks=[{"id":1, "text": "Solve math tools for crypto", "done": False, "pinned": True }, {"id":2, "text": "Clean ur closet", "done": True, "pinned": False }]
@app.route('/')
def hello():
    return render_template("index.html", tasks=tasks)
@app.route('/task/<int:task_num>')
def task(task_num):
    return f"task {task_num}"
@app.route('/add', methods=['POST'])
def add_a_task():
    ids=[]
    for task in tasks:
        ids.append(task["id"])
    task_text=request.form["task"]
    task_text=task_text.strip()
    if task_text=="":
        return redirect(url_for("hello"))
    task_id = max(ids) + 1 if ids else 1
    tasks.append({"id": task_id, "text": task_text, "done": False, "pinned": False })
    return redirect(url_for("hello"))
@app.route('/pin/<int:task_id>', methods=['POST'])
def pin_task(task_id):#the task when its pinned cant go up or down the list of tasks, lazem nssegemha
    for task in tasks:
        if task["id"] == task_id:
            task["pinned"] = not task["pinned"]
            break
    return redirect(url_for("hello"))
@app.route('/done/<int:task_id>', methods=['POST'])
def done_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("hello"))
@app.route('/delete/<int:task_id>')#nzidoou nzirou l action ta3 delete 
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("hello"))
    
