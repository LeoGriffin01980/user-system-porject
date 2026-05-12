users = [
    {
        "username": "leo",
        "password": "123",
        "role": "user"
    },
    {
        "username": "ly",
        "password": "456",
        "role": "user"
    },
    {
        "username": "01980",
        "password": "789",
        "role": "user"
    },
    {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    }
]


def register(users, username, password):
    for user in users:
        if user["username"] == username:
            print("The username already exists")
            return
    users.append({
        "username": username,
        "password": password,
        "role": "user"
    })
    print("Register successful")


def login(users, username, password):
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                print("Login successful")
                return user
            else:
                print("Password error")
                return None
    print("The user does not exist")
    return None


def show_users(users):
    for user in users:
        print(f"username: {user['username']} | role: {user['role']}")


def update_username(users, current_user, new_name):
    for user in users:
        if user["username"] == new_name:
            print("The username is already in use")
            return
    current_user["username"] = new_name
    print("Username updated successfully")


def admin_update_username(users, username, new_name):
    target_user = None
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
    print("Username updated successfully")


def update_password(current_user, new_password):
    current_user["password"] = new_password
    print("Password updated successfully")


def admin_update_password(users, username, new_password):
    for user in users:
        if user["username"] == username:
            user["password"] = new_password
            print("Password updated successfully")
            return
    print("The user does not exist")


def delete_user(users, current_user):
    users.remove(current_user)
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
            return
    print("The user does not exist")


current_user = None


while True:


    print("\n===== USER SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Show Users")
    print("4. Update Password")
    print("5. Update Username")
    print("6. Delete User")
    print("7. Exit")
    print("8. Logout")


    choice = input("Please choose: ")


    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        register(users, username, password)


    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        current_user = login(users, username, password)


    elif choice == "3":
        if current_user is None:
            print("Please login first")
            continue
        if current_user["role"] != "admin":
            print("Permission denied")
            continue
        show_users(users)


    elif choice == "4":


        if current_user is None:
            print("Please login first")
            continue
        if current_user["role"] == "admin":
            username = input("Enter username: ")
            new_password = input("Enter new password: ")
            admin_update_password(users, username, new_password)
        else:
            new_password = input("Enter new password: ")
            update_password(current_user, new_password)


    elif choice == "5":
        if current_user is None:
            print("Please login first")
            continue


        if current_user["role"] == "admin":
            username = input("Enter username: ")
            new_name = input("Enter new username: ")
            admin_update_username(users, username, new_name)


        else:
            new_name = input("Enter new username: ")
            update_username(users, current_user, new_name)


    elif choice == "6":
        if current_user is None:
            print("Please login first")
            continue


        if current_user["role"] == "admin":
            username = input("Enter username: ")
            admin_delete_user(users, username, current_user)

        else:
            delete_user(users, current_user)
            current_user = None


    elif choice == "7":
        print("System exited")
        break


    elif choice == "8":
        if current_user is None:
            print("No user is currently logged in")
        else:
            current_user = None
            print("Logout successful")
    else:
        print("Invalid choice")