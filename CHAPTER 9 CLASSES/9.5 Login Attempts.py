class User():
    """Modelling a user profile"""
    
    def __init__ (self, first_name, last_name, interest, location):
        """Initialize user """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.interest = interest
        self.location = location.title()
        self.login_attempts = 0
        
    def describe_user(self):
        """Summary of user information"""
        print(f"\nFirstname: {self.first_name}")
        print(f"Lastname: {self.last_name}")
        print(f"Interest: {self.interest}")
        print(f"Location: {self.location}")
        print(f"Login_attempts: {self.login_attempts}")
        
    def greet_user(self):
        """Greet user"""
        print("\nAkwaaba " + self.first_name.title()  + "! " +"Happy to have you here ")
        
    
    def increment_login_attempts(self):
        """Increase login attempts by 1"""
        self.login_attempts += 1
               
    def reset_login_attempts(self):
        """Reset login attempts to zero"""
        self.login_attempts = 0
               

user_one = User("emmanuel", "munufie", "robotics", "sunyani")
user_one.describe_user()
user_one.greet_user()



user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print("login attempts:" + str(user_one.login_attempts))
print("login attempts:" + str(user_one.reset_login_attempts()))