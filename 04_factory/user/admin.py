from i_user import IUser

class Admin(IUser):
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.type = "Admin"
    
    def get_name(self):
        return self.name
    
  
    def get_address(self):
        return self.address
    
   
    def get_type(self):
        return self.type
    
    