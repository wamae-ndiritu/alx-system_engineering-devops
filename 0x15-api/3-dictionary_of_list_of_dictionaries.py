#!/usr/bin/python3
"""
Script that returns information about an employee's TODO
list progress from a REST API.
"""
import json
import requests
import sys


def get_employee_todo_progress():
    """
    Gets employee's TODO list progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()

    # Create empty dict for JSON serialization
    obj = {}

    # For all users
    for user in users:
        # Fetch the todo list for a given user
        url = f"{base_url}/todos?userId={user['id']}"
        todos = requests.get(url).json()
        user_todos = [
                {
                    "username": user['username'],
                    "task": task['title'],
                    "completed": task['completed']
                }
                for task in todos
        ]
        # Add the list of dictionaries to the obj
        employee_id = str(user['id'])
        obj[employee_id] = user_todos

    # Write data to JSON
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as json_file:
        json.dump(obj, json_file)


if __name__ == "__main__":
    get_employee_todo_progress()
