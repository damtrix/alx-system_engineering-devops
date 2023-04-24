#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    
    
    response = requests.get(url).json()
    total_tasks = 0
    for i in response:
        if i['userId'] == int(id):
            total_tasks += 1
    
   
    num_lines = 0
    with open(str(id) + ".csv", 'r') as f:
        for line in f:
            if not line == '\n':
                num_lines += 1
                
    print("num_lines: {}".format(num_lines))
    print("Total_tasks: {}".format(total_tasks))
