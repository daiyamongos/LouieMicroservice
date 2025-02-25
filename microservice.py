from flask import Flask, request, jsonify
import json

app = Flask(__name__)

savedTasks = "savedTasks.json"

@app.route("/getTasks", methods=["GET"])
def getTasks():
    # try to load the json file to return to main
    try:
        with open(savedTasks, 'r') as file:
            tasks = json.load(file)
            return jsonify(tasks)
    except(FileNotFoundError):
        return jsonify({"error": "Could not retrieve task list!"}), 400

@app.route("/saveTasks", methods=["POST"])
def saveTasks():

    newTasks = request.json
    
    # check for list parity
    if isinstance(newTasks, list) == False:
        return jsonify({"error": "Not a list!"}), 400
    elif all(isinstance(task, dict) for task in newTasks) == False:
        return jsonify({"error": "A task in the list is not in the form of dict!"}), 400


    # try to save the task list to the json file
    try:
        with open(savedTasks, 'w') as file:
            print("Saving tasks:", newTasks)
            json.dump(newTasks, file, indent=1)
    except:
        return jsonify({"error": "Failed to save to JSON file!"}), 500
    
    # Success yippie!
    return jsonify({"message": "Successfully saved task list!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
