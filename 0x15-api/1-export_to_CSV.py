#!/usr/bin/python3
"""Export data in the CSV format"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = str(argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + user_id).json()
    name = user["name"]
    user_name = user["username"]
    tasks = requests.get(url + "todos?userId=" + user_id).json()
    with open(user_id + ".csv", "w") as file:
        for task in tasks:
            status = task["completed"]
            title = task["title"]
            format = '"{}","{}","{}","{}"\n'.format(user_id, user_name,
                                                    status, title)
            file.write(format)
