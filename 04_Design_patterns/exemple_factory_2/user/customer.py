from i_user import IUser

class Customer(IUser):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.type = "Customer"
        
        
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_type(self):
        return self.type
        
        