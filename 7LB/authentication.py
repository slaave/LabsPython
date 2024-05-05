import hashlib 

def hash_password(password): 
    hashed_password = hashlib.md5(password.encode()).hexdigest() 
    return hashed_password 

class User: 
    def __init__(self, login, password, is_admin=False): 
        self.login = login 
        self.hashed_password = hash_password(password) 
        self.is_admin = is_admin 

    def change_password(self, new_password): 
        self.hashed_password = hash_password(new_password) 