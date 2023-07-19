class Restaurant():
    """Modelling a restaurant"""
    
    def __init__ (self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name.title()
        self.cuisine = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
     """Welcome message of restaurant"""   
     print(self.name.title() + " is open and welcomes you")
         
    def open_restaurant(self):
     """Display food available """
     print(self.name.title() + " has " + self.cuisine + " available.")
    
    def set_number_served(self, number_served):
        """Set the number of customers served"""
        self.number_served = number_served
    
    def increment_number_served(self, more_customers):
        """Increment number of customers served"""
        self.number_served += more_customers
    
    
    

        
restaurant = Restaurant("imperial lotus", "japanese fried rice")
restaurant.open_restaurant()

print("\n" +  str(restaurant.number_served) + " customers have been served." )


restaurant.number_served = 50
print("\n" +  str(restaurant.number_served) + " customers have been served." )

restaurant.number_served = 100
print("\n" +  str(restaurant.number_served) + " customers have been served." )

restaurant.increment_number_served(150)
print("\n" +  str(restaurant.number_served) + " customers have been served." )

