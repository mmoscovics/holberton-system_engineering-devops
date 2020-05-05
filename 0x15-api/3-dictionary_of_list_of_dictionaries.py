#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    for user in users:
        user_id = str(user["id"])
        name = user["name"]
        tasks = requests.get(url + "todos?userId=" + user_id).json()
        task_list = []
        for task in tasks:
            task_list.append({"task": task["title"],
                              "completed": task["completed"],
                              "username": user["username"]})
        task_dict = {}
        task_dict[user_id] = task_list
    with open("todo_all_employees.json", "w") as file:
        json.dump(task_dict, file)
