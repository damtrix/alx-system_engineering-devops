#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    response = requests.get(url)
    employeeUserName = response.json().get('username')
    todosUrl = url + "/todos"
    response = requests.get(todosUrl)
    todos = response.json()
    with open("{}.csv".format(str(employeeId)), 'w') as file:
        for todo in todos:
            if todo:
                file.write('"{}","{}","{}","{}"\n'.format(
                    str(employeeId), employeeUserName, todo.get(
                        'completed'), todo.get('title')))
