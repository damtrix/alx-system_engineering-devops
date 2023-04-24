#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import json


if __name__ == "__main__":
    usersUrl = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(usersUrl)
    users = response.json()
    dict = {}
    for user in users:
        userId = user.get('id')
        username = user.get('name')
        userTodosUrl = usersUrl + "{}".format(userId) + "/todos/"
        response = requests.get(userTodosUrl)
        userTodos = response.json()
        dict[userId] = []
        for todo in userTodos:
            dict[userId].append({"task": todo.get("title"),
                                 "completed": todo.get("completed"),
                                 "username": username})

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(dict, jsonfile)
