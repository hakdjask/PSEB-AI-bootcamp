# Task 01: API (GitHub)

import requests

a = requests.get('https://api.github.com/users/morluto')
b = requests.get('https://api.github.com/users/pbakaus')
c = requests.get('https://api.github.com/users/yetone')

print(a.status_code, b.status_code, c.status_code, "\n")

print("Person A: ", a.json() ["login"], a.json() ["public_repos"], "\n")
print("Person B: ", b.json() ["login"], b.json() ["public_repos"], "\n")
print("Person C: ", c.json() ["login"], c.json() ["public_repos"], "\n")