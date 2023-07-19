class Restaurant():
    """Modelling a restaurant"""
    
    def __init__ (self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name.title()
        self.cuisine = cuisine
        
    def describe_restaurant(self):
     """Welcome message of restaurant"""   
     print(self.name.title() + " is open and welcomes you")
         
    def open_restaurant(self):
     """Display food available """
     print(self.name.title() + " has " + self.cuisine + " available.")


restaurant = Restaurant("imperial lotus", "japanese fried rice")


restaurant.describe_restaurant()
restaurant.open_restaurant()
     
