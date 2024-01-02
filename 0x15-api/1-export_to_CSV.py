#!/usr/bin/python3
"""
Script that returns information about an employee's TODO
list progress from a REST API.
"""
import sys
import requests
import csv


def get_employee_todo_progress(employee_id):
    """
    Gets employee's TODO list progress
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

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write csv header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write data to csv
        for task in todo_list:
            csv_writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
