from validators import validate_password,validate_username
from data import save_users
from security import hash_password




def register(users, username, password):
    username = validate_username(username)
    password = validate_password(password)
    if username is None or password is None:
        return
    for user in users:
        if user["username"] == username:
            print("The username already exists")
            return
    password = hash_password(password)    
    users.append({
        "username": username,
        "password": password,
        "role": "user",
        "login_fail_count" : 0,
        "locked" : False
    })
    save_users(users)
    print("Register successful")


def login(users, username, password):
    username = username.strip()
    password = password.strip()
    if username is None or password is None:
        return None 
    for user in users:
        if user["username"] == username:
            if user["locked"]:
                print("this account is locked")
                return None
            if user["password"] == hash_password(password) :
                user["login_fail_count"] = 0
                save_users(users)    
                print("Login successful")
                return user
            else:
                user["login_fail_count"] += 1
                print("password error")
                save_users(users)
                if user["login_fail_count"] >= 3:
                    user["locked"] = True
                    save_users(users)
                    print("password error.this account has been locked")
                return None 
    print("The user does not exist")
    return None


def show_users(users):
    for user in users:
        print(f"username: {user['username']} | role: {user['role']}")


def update_username(users, current_user, new_name):
    new_name = validate_username(new_name)
    if new_name is None:
        return
    for user in users:
        if user["username"] == new_name:
            print("The username is already in use")
            return
    current_user["username"] = new_name
    save_users(users)
    print("Username updated successfully")


def admin_update_username(users, username, new_name):
    target_user = None
    new_name = validate_username(new_name)
    if new_name is None:
        return
    for user in users:
        if user["username"] == username:
            target_user = user
            if user["role"] == "admin":
                print("You can not update admin username")
                return
        if user["username"] == new_name:
            print("The username is already in use")
            return
    if target_user is None:
        print("The user does not exist")
        return
    target_user["username"] = new_name
    save_users(users)
    print("Username updated successfully")


def update_password(users,current_user,new_password):
    new_password = validate_password(new_password)
    if new_password is None:
        return
    current_user["password"] = hash_password(new_password) 
    save_users(users)
    print("Password updated successfully")


def admin_update_password(users, username, new_password):
    new_password = validate_password(new_password)
    if new_password is None:
        return
    for user in users:
        if user["username"] == username:
            user["password"] = hash_password(new_password)
            save_users(users)
            print("Password updated successfully")
            return
    print("The user does not exist")


def delete_user(users, current_user):
    users.remove(current_user)
    save_users(users)
    print("User deleted successfully")


def admin_delete_user(users, username, current_user):
    if current_user["username"] == username:
        print("You can not delete yourself")
        return
    for user in users:
        if user["username"] == username:
            if user["role"] == "admin":
                print("You can not delete another admin")
                return
            users.remove(user)
            print("User deleted successfully")
            save_users(users)
            return
    print("The user does not exist")


def admin_unlock_user(users,username):
    for user in users:
        if user["username"] == username:
            user["locked"] = False
            user["login_fail_count"] = 0
            save_users(users)
            print("user unlocked successfully")
            return
    print("the user does not exist")    
current_user = None