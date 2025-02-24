from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

currentTasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=currentTasks)

@app.route('/addTasks', methods=['POST'])
def addTasks():
    task_name = request.form['taskName']
    task_value = request.form['taskValue']
    newEntry = {task_name: task_value}
    currentTasks.update(newEntry)
    return redirect(url_for('index'))

@app.route('/saveTasks', methods=['POST'])
def saveTasks():
    response = requests.post('http://127.0.0.1:5000/updateTasks', json=currentTasks)
    result = response.json()
    return redirect(url_for('index'))

@app.route('/loadTasks', methods=['GET'])
def loadTasks():
    response = requests.get('http://127.0.0.1:5000/getTasks')
    tasks = response.json()
    currentTasks.update(tasks)
    return render_template('index.html', tasks=currentTasks)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
