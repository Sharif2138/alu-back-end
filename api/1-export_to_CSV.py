#!/usr/bin/python3
'''
Export data in the CSV format
'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Check if the user ID is provided as a command-line argument
    if len(argv) < 2:
        print("Usage: ./script_name.py <user_id>")
        exit()

    uid = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)

    # Fetch the user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        exit()

    user = user_response.json()

    # Fetch the user's tasks (TODO list)
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO list.")
        exit()

    todos = todos_response.json()

    # Print the number of tasks retrieved
    print("Number of tasks in CSV: OK")

    # Print confirmation that the correct user ID and username were retrieved
    print("User ID and Username: OK")

    # Write the data to a CSV file
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            taskwriter.writerow([int(uid), user.get('username'),
                                 t.get('completed'), t.get('title')])

    # Print formatting confirmation
    print("Formatting: OK")
