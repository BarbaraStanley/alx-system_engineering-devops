#!/usr/bin/python3
''' Python script to export employee data in the JSON format '''

import json
import requests
import sys

if __name__ == "__main__":
    eid = sys.argv[1]
    filename = eid+'.json'
    userid = eid
    task =  requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': eid}).json()

    username = requests.get('https://jsonplaceholder.typicode.com/users', params={'id': eid}).json()

    usernam = username[0]['username']

    task_cs = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': eid}).json()


    newlist = []
    main = {}

    for i in task_cs:
        new = {}
        #new['userid'] = userid
        new['task'] = i['title']
        new['completed'] = i['completed']
        new['username'] = usernam

        newlist.append(new)

    main[userid] = newlist
    print(main)

    #with open(filename, 'w') as f:
        #writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        #writer.writerows(newlist)

    #Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

    with open(filename, mode="w") as json_file:
        json.dump(main, json_file)
