import requests

r = requests.get('https://api.github.com/users/octocat')

print(r.status_code)
print(r.json() ["login"], "\n")

hamza = requests.get('https://api.github.com/users/hakdjask')

data = hamza.json()
print(data["login"], data["id"], data["public_repos"], "\n")