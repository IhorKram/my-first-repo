#!/usr/bin/python3
import sys
import requests
# get and print my github id with username and password passed as arguments
url = "https://api.github.com/user"
username = sys.argv[1]
password = sys.argv[2]
response = requests.get(url, auth=(username, password))
if response.status_code == 200:
    print(response.json()["id"])
else:
    print("None")


