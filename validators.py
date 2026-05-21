blocked_names = ["admin","root","none","null"]

def validate_username(username):
    username = username.strip()
    if not username:
        print("username can not be empty")
        return None
    if len(username) >8 or len(username) <3:
        print("username must be 3 to 8 chartes long")
        return None
    if username.lower() in blocked_names:
        print("the user name can not use")
        return None     
    return username   


def validate_password(password):
    password = password.strip()
    if not password:
        print("password can not be empty")
        return None
    if len(password) > 12 or len(password) < 6:
        print("password must be 6 to 12 chartes long")
        return None
    return password        


