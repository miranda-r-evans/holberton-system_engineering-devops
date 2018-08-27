#!/usr/bin/python3
'''
script to save task information in csv format
'''

import requests
from sys import argv

if __name__ == "__main__":

    emp_id = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(emp_id))
    emp_name = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == emp_id]

    with open('2.csv', 'w+') as f:
        for item in all_tasks:
            f.write('"{}","{}","{}","{}"\n'.format(emp_id, emp_name,
                                                   item.get('completed'),
                                                   item.get('title')))
