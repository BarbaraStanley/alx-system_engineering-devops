#!/usr/bin/python3
''' Python script to export employee data in the CSV format given emplyee id'''

import csv
import requests
import sys

if __name__ == "__main__":
    eid = sys.argv[1]

    userid = eid
    username = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(eid)).json()
    
    task_cs = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': eid}).json()
    
    filename = eid+'.csv'
    newlist = []

    for i in task_cs:
        new = []
        new.append(userid)
        new.append(username.get('username'))
        new.append(i['completed'])
        new.append(i['title'])
        newlist.append(new)

    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(newlist)
