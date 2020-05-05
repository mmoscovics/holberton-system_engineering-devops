#!/usr/bin/python3
"""Export data in the JSON format"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + user_id).json()
    name = user["name"]
    tasks = requests.get(url + "todos?userId=" + user_id).json()
    task_list = []
    for task in tasks:
        task_list.append({"task": task["title"],
                          "completed": task["completed"],
                          "username": user["username"]})
    task_dict = {}
    task_dict[user_id] = task_list
    with open(user_id + ".json", "w") as file:
        json.dump(task_dict, file)
