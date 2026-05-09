class User:
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role

users = []
users.append(User("leo","123","user"))
users.append(User("ly","456","user"))
users.append(User("01980","789","user"))
users.append(User("admin","admin123","admin"))


def register(users,username,password):
    found = False
    for user in users:
        if user.username == username:
            found = True
            print("The user name already exsits")
            break
 
    if  not found :
        users.append(User(username,password,"user"))
        print("Register successfully")


def login(users,username,password):

    found = False
    for user in users:
        if user.username == username:
            found = True
            if user.password == password:
                print("login successful")
                return user
            else:
                print("Password error")
                return None           

    if not found:
        print("The user does not exist")
        return None


def show_users(users):
    for user in users:
        print(f"{user.username}-{user.role}")


def update_password(user,new_password):   
         user.password = new_password
         print("update pssword succeeded")        


def admin_update_password(users,username,new_password):
    found = False
    for user in users:
        if user.username == username:
            found = True 
            user.password = new_password
            print("password update successfully")
            break
    if not found:
        print("the user does not exist")    


def delete_user(users,user):
    users.remove(user)
    print("deletion succeeded")


def admin_delete_user(users,username,current_user):
    found = False
    if current_user.username == username:
        print("you can not delete yourslef")
        return
    for user  in users:
           if user.username == username:
                found = True
                users.remove(user)
                print("delete succeeded")
                break
    if not found:        
        print("the user does not exist")
        

current_user = None
while True:


    print("1.register 2.login 3.show users 4.update password 5.delete user 6.out 7.logout")


    choice = input("please choice")


    if choice == "1":
        username = input("Please enter user name")
        password = input("Pleaswe enter password")
        register(users,username,password)


    elif choice == "2" :
        username = input("Please enter user name")
        password = input("Please enter password")
        current_user = login(users,username,password)

    
    elif choice == "3":        
        if current_user is None:
            print("plaease login first")
            continue
        if current_user.role != "admin":
            print("Permission denied")
            continue 
        show_users(users)
            



    elif choice == "4":
        if current_user is None:
            print("plaease login first")
            continue   
        if current_user.role == "admin":
            username = input("please enter user name")
            new_password = input("plwase enter new password")
            admin_update_password(users,username,new_password)
        else:                      
            new_password = input("please enter new password")
            update_password(current_user,new_password)
            


    elif choice == "5":
        if current_user is None:
            print("plaease login first")
            continue
        if current_user.role == "admin":
            username = input("please enter user")
            admin_delete_user(users,username)
        else:
            delete_user(users,current_user)
            current_user = None
        
        
    elif choice == "6":
        print("out")
        break


    elif choice =="7":
         if current_user is None:
            print("No user is currently logged in")
         else:
            current_user = None
            print("logout successful")

    
