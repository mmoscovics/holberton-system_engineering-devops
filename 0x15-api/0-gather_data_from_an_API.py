#!/usr/bin/python3
"""Using this REST API, for given employee ID, returns to do list progress"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + argv[1]).json()
    name = user["name"]
    tasks = requests.get(url + "todos?userId=" + argv[1]).json()
    done = 0
    total = 0
    for task in tasks:
        if task["completed"] is True:
            done += 1
        total += 1
    titles = [task for task in tasks if task["completed"] is True]
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for title in titles:
        print("\t {}".format(title["title"]))
