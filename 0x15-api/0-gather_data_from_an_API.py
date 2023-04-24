#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    response = requests.get(url)
    employeeName = response.json().get('name')
    todosUrl = url + "/todos"
    response = requests.get(todosUrl)
    todos = response.json()
    no_done_tasks = 0
    do_tasks = []
    for todo in todos:
        if todo.get('completed'):
            do_tasks.append(todo)
            no_done_tasks += 1
    print("Employee {} is done with tasks({}/{})".format(
        employeeName, no_done_tasks, len(todos)))
    for task in do_tasks:
        print("\t {}".format(task.get('title')))
