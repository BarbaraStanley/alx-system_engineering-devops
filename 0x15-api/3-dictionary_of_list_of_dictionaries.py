#!/usr/bin/python3
''' Python script to export employee data in the JSON format '''

import json
import requests
import sys

if __name__ == "__main__":

    task = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    task_cs = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    main = {}

    for u in users:
        newlist = []
        for i in task_cs:
            if i['userId'] == u['id']:
                new = {}
                new['task'] = i['title']
                new['completed'] = i['completed']
                new['username'] = u['username']
                newlist.append(new)
        main[u['id']] = newlist

    print(main)

    # with open(filename, 'w') as f:
    # writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    # writer.writerows(newlist)

    # Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
    # TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
    # "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

    with open('todo_all_employees.json', mode="w") as json_file:
        json.dump(main, json_file)
