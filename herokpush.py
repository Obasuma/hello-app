import requests

new_req = "http://id.heroku.com"

logins = {"username": "orinayobra@gmail.com", "password": "pass"}

obj = requests.get(new_req, logins).json()

print(obj)
