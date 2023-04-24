#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
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
    with open("{}.json".format(employeeId), 'w') as jsonFile:
        json.dump({
            employeeId: [{
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": employeeUserName} for todo in todos]}, jsonFile)
