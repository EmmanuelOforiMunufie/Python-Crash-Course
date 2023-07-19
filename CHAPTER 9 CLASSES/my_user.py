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





             


