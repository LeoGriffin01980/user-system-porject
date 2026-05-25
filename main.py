from auth import register,login,show_users,admin_delete_user,admin_update_password,admin_update_username,update_password,update_username,delete_user,admin_unlock_user
from data import load_users
users = load_users()
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
    print("9. unlock")
    print("=========================")


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
            update_password(users,current_user, new_password)


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


    elif choice == "9":
        if current_user is None:
            print("please login first")
            continue
        if current_user["role"] != "admin":
            print("permission denied")
            continue
        username = input("enter username")
        admin_unlock_user(users,username)
         


    