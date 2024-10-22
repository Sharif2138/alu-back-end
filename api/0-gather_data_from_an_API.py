#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests

get_todos(employee_id):
user_data = requests.get(f"{USERS_URL}/{employee_id}").json()
todos = requests.get(TODO_URL).json()
employee_name = user_data["name"]
employee_todo = []
completed_emp_todos = []
completed_totods_title = []

for todo in todos:
    if todo["userId"] == employee_id:
        employee_todo.append(todo)
    if todo["completed"] == True and todo ["userId"] == employee_id:
        completed_emp_todos.append(todo)
for todo in completed_emp_todos:
    if todo["userId"] == employee_id:
        completed_totods_title.append(todo["title"])
print(f"Employee {employee_name} is done with tasks({len(completed_totods_title)}):")
for title in completed_totods_title:
    print(title)
