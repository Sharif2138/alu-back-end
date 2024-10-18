#!/usr/bin/env python3
"""
0-gather_data_from_an_API.py

This script fetches data from a REST API and displays the progress of an employee's TODO list.
It uses the provided employee ID to get the employee's name and list of tasks, displaying:
1. The employee's name.
2. The number of completed tasks versus the total number of tasks.
3. The titles of completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Where <employee_id> is an integer representing the employee whose TODO list should be retrieved.

Requirements:
    - Python 3.x
    - The 'requests' module (can be installed using 'pip install requests')
"""

import requests
import sys

def get_employee_todo_list(employee_id):
    """
    Fetch and display the TODO list progress for a given employee.

    Parameters:
        employee_id (int): The ID of the employee whose TODO list is to be retrieved.

    Returns:
        None: Prints the output to the standard output.

    The function fetches the employee's name and the list of tasks from the API. It then calculates
    the total number of tasks and the number of tasks that are marked as completed. It displays this
    information along with the titles of the completed tasks in the required format.
    """
    # Step 1: Fetch employee data from the API
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Step 2: Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for user with ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Step 3: Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    # Step 4: Display the output in the specified format
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    """
    The main entry point of the script.

    This section checks if the script is being executed directly (not imported as a module).
    It validates the command-line arguments to ensure an employee ID is provided and is an integer.
    If valid, it calls the get_employee_todo_list() function with the provided employee ID.
    """
    # Check if the script received the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Try converting the first argument to an integer for the employee ID
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    # Call the function to gather and display data
    get_employee_todo_list(employee_id)
