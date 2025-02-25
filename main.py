import requests
import json

BASE_URL = "http://127.0.0.1:5000"  # Update if running on a different port


def save_tasks(tasks):
    """Sends a POST request to save tasks to the server"""
    response = requests.post(f"{BASE_URL}/saveTasks", json=tasks)
    print("Save Tasks Response:", response.status_code, response.json())


def get_tasks():
    """Sends a GET request to retrieve saved tasks from the server"""
    response = requests.get(f"{BASE_URL}/getTasks")
    print("Get Tasks Response:", response.status_code, response.json())


def test_task_list():
    """Test saving and retrieving a valid task list"""
    print("\n--- Running Valid Task List Test ---")
    valid_tasks = [
        {"task": "Buy groceries", "completed": False},
        {"task": "Walk the dog", "completed": True},
        {"task": "Study for exam", "completed": False},
        {"task": "Go to the gym", "completed": True},
        {"task": "Call mom", "completed": False},
    ]
    
    save_tasks(valid_tasks)
    get_tasks()


def test_invalid_data():
    """Test saving invalid data (not a list)"""
    print("\n--- Running Invalid Data Test ---")
    
    invalid_tasks = {"task": "This is not a list!"}  # Should fail
    save_tasks(invalid_tasks)  # Expecting error

    invalid_tasks = [1, 2, 3, "string"]  # Should also fail
    save_tasks(invalid_tasks)  # Expecting error


def test_empty_list():
    """Test saving an empty task list"""
    print("\n--- Running Empty Task List Test ---")
    empty_tasks = []
    
    save_tasks(empty_tasks)
    get_tasks()


if __name__ == "__main__":
    print("Starting tests...")

    test_task_list()
    test_invalid_data()
    test_empty_list()
    
    print("\nAll tests completed.")
