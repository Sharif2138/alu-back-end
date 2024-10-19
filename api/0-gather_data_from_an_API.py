#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""

import requests
import sys

def fetch_employee_name(api_url, employee_id):
    """Fetch the employee's name using the given employee ID."""
    response = requests.get(f"{api_url}/users/{employee_id}")
    if response.status_code != 200:
        print(f"RequestError: Unable to find employee with ID {employee_id}.")
        sys.exit(1)
    user_data = response.json()
    return user_data.get("name")

def fetch_employee_todos(api_url, employee_id):
    """Fetch the TODO list for the specified employee."""
    response = requests.get(f"{api_url}/users/{employee_id}/todos")
    if response.status_code != 200:
        print(f"RequestError: Unable to fetch TODO list for employee ID {employee_id}.")
        sys.exit(1)
    return response.json()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    if not EMPLOYEE_ID.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
        
    EMPLOYEE_ID = int(EMPLOYEE_ID)

    try:
        # Get the employee's name
        employee_name = fetch_employee_name(API_URL, EMPLOYEE_ID)
        
        # Get the list of tasks for the employee
        todos = fetch_employee_todos(API_URL, EMPLOYEE_ID)
        
        if not todos:
            print(f"No TODO tasks found for employee ID {EMPLOYEE_ID}.")
            sys.exit(1)

        # Calculate the number of completed tasks
        total_tasks = len(todos)
        completed_tasks = [task for task in todos if task["completed"]]
        number_of_done_tasks = len(completed_tasks)

        # Print the output in the required format
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"NetworkError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
