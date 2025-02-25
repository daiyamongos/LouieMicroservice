# LouieMicroservice

A microservice to create persistent task lists for Louie

It allow for task list retrieval (using /getTasks) as well as task list saving to a JSON file (using /saveTasks)

# Communication Contract:
a **POST** request from the main program side would look like:

## example of sending task list to microservice A (with HTTP POST request)

### Sample task list
```
tasks_list = [
    {"task": "Buy groceries", "desc": "Keep within your weekly budget"},
    {"task": "Walk the dog", "desc": "Walk at least a mile"},
    {"task": "Weekly Study Session", "desc": "Make sure to study chapter 8-10"}
]
```
### URL of the POST microservice
```
url = "http://localhost:5000/saveTasks"

tasks_list=[{},{},...,{}]
response = requests.post(f"{url}/saveTasks", json=tasks)

print(response)
```

## example outputs

### on SUCCESS
```
{
  "message": "Successfully saved task list!"
}
```
### on FAILURE

if the task list is not of type list
```
{
  "error": "Not a list!"
}
```
if any task in the task list is not of type dict
```
{
  "error": "A task in the list is not in the form of dict!"
}
```
if the microservice cannot save the task list to savedTasks.json for any reason
```
{
  "error": "Failed to save to JSON file!"
}
```
## example of retrieving task list from microservice A (with HTTP GET request)

```
### URL of the GET microservice
url = "http://localhost:5000/getTasks"

response = requests.get(url)

''' this is checking that it is not an error message before setting the task list '''
if isinstance(response, dict) == False: 
    tasks_list = response

print(tasks_list)
```

### example outputs

### on SUCCESS
```
[
    {"task": "Buy groceries", "desc": "Keep within your weekly budget"},
    {"task": "Walk the dog", "desc": "Walk at least a mile"},
    {"task": "Weekly Study Session", "desc": "Make sure to study chapter 8-10"}
]
```
### on FAILURE

if the task list retrieval failed
```
{
    'error': "Could not retrieve task list!"
}
```
# Setup / Running Microservice

It isn't a lot of setup to be honest. It should be run locally on a virtual environment. I assume since Louie is using flask he will already have all of this setup for his project but will still list it in case.

create virtual environment
```
virtualenv venv
```

> this may not apply if you are using windows
activate virtual environment (for macOS)
```
source venv/bin/activate
```

> May not need to do this since you will probably already have yours setup
make sure to install any required packages for the virtual environment
```
pip install -r requirements.txt
```

## Running Microservice

```
python3 microservice.py
```

