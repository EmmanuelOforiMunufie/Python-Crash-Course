class User():
    """Modelling a user profile"""
    
    def __init__ (self, first_name, last_name, interest, location):
        """Initialize user """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.interest = interest.title()
        self.location = location.title()
    
    def describe_user(self):
        """Summary of user information"""
        print(f"\nfirstname: {self.first_name}")
        print(f"lastname: {self.last_name}")
        print(f"interest: {self.interest}")
        print(f"location: {self.location}")
        print("\n")
        
    def greet_user(self):
        """Greet user"""
        print("Akwaaba " + self.first_name.title()  + "! " +"Happy to have you here ")   

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


user_one = Admin("emmanuel", "munufie", "robotics", "sunyani")
user_one.describe_user()


print("\nAdding privileges...")
user_one.privileges = [
    "can start a trend",
    "can take down offensive posts",
    "can moderate conversations "
    ]               


user_one.show_privileges()