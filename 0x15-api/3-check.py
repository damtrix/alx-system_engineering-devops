#!/usr/bin/python3
"""
Gather data about employees TODO and export to JSON
"""
import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Fetch user info """
    
    from collections import defaultdict
    correct_output = defaultdict(list)

    response = requests.get(todos_url).json()
    for item in response:
        url = users_url + str(item['userId'])
        usr_resp = requests.get(url).json()
        correct_output[item['userId']].append(
            {'username': usr_resp[0]['username'],
            'completed': item['completed'],
            'task': item['title']})

    with open('todo_all_employees.json', 'r') as f:
        student_output = json.load(f)

    error = False
    for correct_key, correct_entry in correct_output.items():
        flag = 0
        for student_key, student_entry in student_output.items():
            if str(correct_key) == str(student_key):
                flag = 1
                if correct_entry != student_entry:
                    print("User ID {} Tasks: Incorrect".format(str(correct_key)))
                    error = True
        if flag == 0:
            print("User ID {}: Not found".format(str(correct_key)))
            error = True

    if not error:
        print("User ID and Tasks output: OK")

if __name__ == "__main__":
    user_info()