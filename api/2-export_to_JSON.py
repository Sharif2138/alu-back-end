#!/usr/bin/python3
'''
Exports user tasks to a JSON file in the specified format.
'''

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    uid = sys.argv[1]  # User ID from command-line argument

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{uid}"
    user_response = requests.get(user_url, verify=False)
    if user_response.status_code != 200:
        print(f"User with ID {uid} not found.")
        sys.exit(1)

    user = user_response.json()
    username = user.get('username')

    # Fetch tasks for the user
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"
    tasks_response = requests.get(tasks_url, verify=False)
    if tasks_response.status_code != 200:
        print("Could not fetch tasks for the user.")
        sys.exit(1)

    tasks = tasks_response.json()

    # Format the data
    tasks_list = [{"task": task["title"], "username": username, "completed": task["completed"]} for task in tasks]
    data = {str(uid): tasks_list}  # Ensure user ID is a string in the JSON output

    # Export to JSON file
    filename = f"{uid}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

    print(f"Data has been exported to {filename}")
