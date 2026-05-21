import json
from security import hash_password


def save_users(users):
    with open("users.json","w") as file:
        json.dump(users,file)


def load_users():
   try:
       with open("users.json","r") as file:
            users = json.load(file)
            return users
   except:
       users = [{
           "username" : "admin",
           "password" : hash_password("admin123"),
           "role" : "admin",
           "login_fail_count" : 0,
           "locked" : False

       }]
       save_users(users)
       return users
   

users = load_users()