"""
Microservice A for Louie's portfolio project


"""

from flask import Flask, jsonify, request
import json

micro = Flask(__name__)

masterTaskList = {
}

@micro.route('/getTasks', methods=['GET'])
def getTasks():
    return jsonify(masterTaskList)

@micro.route('/updateTasks', methods=['POST'])
def updateTasks():
    global masterTaskList
    masterTaskList = request.json
    print("saved tasks successfully yippieeee!")
    return jsonify({"message": "Saved Tasks Successfully"})

if __name__ == "__main__":
    micro.run(debug=True)