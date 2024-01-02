# 0x15. API

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Scripting](https://img.shields.io/badge/Scripting-Enabled-green.svg)]()
[![Back-end](https://img.shields.io/badge/Back--end-Flask-brightgreen.svg)]()
[![API](https://img.shields.io/badge/API-REST-orange.svg)]()

| Task | Description | File |
|------|-------------|------|
| 0 | Gather data from an API | [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py) |
| 1 | Export to CSV | [1-export_to_CSV.py](./1-export_to_CSV.py) |
| 2 | Export to JSON | [2-export_to_JSON.py](./2-export_to_JSON.py) |
| 3 | Dictionary of list of dictionaries | [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py) |


## Gather data from an API
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

### Requirements
- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:
- First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS)`:
	- `EMPLOYEE_NAME`: name of the employee
	- `NUMBER_OF_DONE_TASKS`: number of completed tasks
	- `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
- Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the TASK_TITLE)

### Usage
```
python3 gather_data_from_api.py <employee_id>
```

### Output Format
```
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
```

## Export to CSV
Using what you did in the task #0, extend your Python script to export data in the CSV format.

### Requirements:

- Records all tasks that are owned by this employee
- Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- File name must be: `USER_ID.csv`

### Example Usage
```
python3 1-export_to_CSV.py 2
```

### Example Output
```
cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
"2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
"2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"
"2","Antonette","True","aliquam aut quasi"
"2","Antonette","True","veritatis pariatur delectus"
"2","Antonette","False","nesciunt totam sit blanditiis sit"
"2","Antonette","False","laborum aut in quam"
"2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
"2","Antonette","False","repudiandae totam in est sint facere fuga"
"2","Antonette","False","earum doloribus ea doloremque quis"
"2","Antonette","False","sint sit aut vero"
"2","Antonette","False","porro aut necessitatibus eaque distinctio"
"2","Antonette","True","repellendus veritatis molestias dicta incidunt"
"2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
"2","Antonette","False","sunt cum tempora"
"2","Antonette","False","totam quia non"
"2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
"2","Antonette","True","totam atque quo nesciunt"
```

## Export to JSON
Using what you did in the task #0, extend your Python script to export data in the JSON format.

### Requirements:

- Records all tasks that are owned by this employee
- Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- File name must be: `USER_ID.json`

### Example Usage
```
2-export_to_JSON.py 2
```

### Example Output
```
cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}
```

## Dictionary of list of dictionaries
Using what you did in the task #0, extend your Python script to export data in the JSON format.

### Requirements:

- Records all tasks from all employees
- Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
- File name must be: `todo_all_employees.json`

### Example usage
```
3-dictionary_of_list_of_dictionaries.py
cat todo_all_employees.json
```
