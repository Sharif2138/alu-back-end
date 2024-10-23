#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    try:
        # Get employee details
        user_response = requests.get(f"{API_URL}/users/{EMPLOYEE_ID}")
        if user_response.status_code != 200:
            print("RequestError: User not found")
            sys.exit(1)

        user_data = user_response.json()
        employee_name = user_data["name"]

        # Get the TODO list for the employee
        todos_response = requests.get(
            f"{API_URL}/todos", params={"userId": EMPLOYEE_ID}
        )
        if todos_response.status_code != 200:
            print("RequestError: Could not retrieve tasks")
            sys.exit(1)

        todos_data = todos_response.json()
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task["completed"]]
        total_done_tasks = len(done_tasks)

        # Display the progress
        print(f"Employee {employee_name} is done with tasks"
              f"({total_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")

    except requests.RequestException as e:
        print(f"RequestError: {e}")
        sys.exit(1)
