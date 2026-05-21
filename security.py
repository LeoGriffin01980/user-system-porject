import hashlib

def hash_password(password):
    password = password.encode()
    return hashlib.sha256(password).hexdigest()