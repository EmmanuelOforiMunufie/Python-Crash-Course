from my_user import User
 
class Admin(User):
    """The Administrator of the group"""
    
    def __init__(self,first_name, last_name, interest, location ):
        """Initialize the admin"""
        super().__init__(first_name, last_name, interest, location)
        
        #initializing an empty set of privileges
        self.privileges = Privileges()
    
    def show_privileges(self):
        """Display Administrator's privileges"""
        
        if self.privileges:
            for privilege in self.privileges:
                print( "The Administrator " + privilege)
     

class Privileges():
    """A simple attempt to model privileges for the Administrator """ 
    
    def ___init__(self,privileges =[]):
        self.privileges = privileges
        
        
    def show_privileges(self):
        """Display Administrator's privileges"""
        
        if self.privileges:
            for privilege in self.privileges:
                print( "The Administrator " + privilege)


           


