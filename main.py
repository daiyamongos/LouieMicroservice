import requests
import json

url = "http://127.0.0.1:5000"

def save_tasks(tasks):
    response = requests.post(f"{url}/saveTasks", json=tasks)
    print("Save Tasks Response:", response.status_code, response.json())


def get_tasks():
    response = requests.get(f"{url}/getTasks")
    print("Get Tasks Response:", response.status_code, response.json())


def test_task_list():
    tasks_list = [
    {"task": "Buy groceries", "desc": "Keep within your weekly budget"},
    {"task": "Walk the dog", "desc": "Walk at least a mile"},
    {"task": "Weekly Study Session", "desc": "Make sure to study chapter 8-10"}
    ]
    
    save_tasks(tasks_list)
    get_tasks()


def test_invalid_data():
    invalid_tasks = {"task": "This is not a list!"} 
    save_tasks(invalid_tasks)

    invalid_tasks = [1, 2, 3, 4, 5, 6, "string"] 
    save_tasks(invalid_tasks) 


def test_empty_list():
    empty_tasks = []
    
    save_tasks(empty_tasks)
    get_tasks()


if __name__ == "__main__":
    print("Starting tests...")

#    test_task_list()
#    test_invalid_data()
    test_empty_list()
    
    print("\nAll tests completed.")
