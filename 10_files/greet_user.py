import json

filename = 'username.json'

with open(filename, 'r') as f:
    user = json.load(f)
    print(f"welcome, {user}")