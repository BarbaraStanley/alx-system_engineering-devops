#!/usr/bin/python3
''' Python script that for a given employee ID, returns TODO list progress '''

import requests
import sys

if __name__ == "__main__":
    eid = sys.argv[1]

    name = {'id': eid}
    title = {'userId': eid, 'completed': 'true'}
    total = {'userId': eid}

    employee_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(eid)).json()
    notask = requests.get('https://jsonplaceholder.typicode.com/todos', params=title).json()
    total_notask = requests.get('https://jsonplaceholder.typicode.com/todos', params=total).json()
    task_title = requests.get('https://jsonplaceholder.typicode.com/todos', params=title).json()

    titlee = [tit['title'] for tit in task_title if 'title' in tit]
    
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name.get("name"), len(notask), len(total_notask)))
    for t in titlee:
        print("\t {}".format(t))
