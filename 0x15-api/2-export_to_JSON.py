#!/usr/bin/python3
"""
Script that returns information about an employee's TODO
list progress from a REST API.
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Gets employee's TODO list progress and export
    data to a JSON file
    """
    base_url = "https://jsonplaceholder.typicode.com"
    res = requests.get(f"{base_url}/todos?userId={employee_id}")

    if res.status_code != 200:
        return

    todo_list = res.json()
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    total_completed_tasks = len(completed_tasks)

    user_info_response = requests.get(f"{base_url}/users/{employee_id}")
    user_info = user_info_response.json()
    employee_name = user_info.get("name", "Unknown")

    print(f"Employee {employee_name} is done with tasks(" +
          f"{total_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")

    # Create JSON data
    username = user_info.get("username")
    json_data = {str(employee_id): [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        for task in todo_list
    ]}

    # Export data to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as j_file:
        json.dump(json_data, j_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
