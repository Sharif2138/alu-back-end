#!/usr/bin/python3
import requests
import sys

def get_employee_todo_list(employee_id):
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