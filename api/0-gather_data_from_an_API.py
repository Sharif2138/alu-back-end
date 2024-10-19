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
