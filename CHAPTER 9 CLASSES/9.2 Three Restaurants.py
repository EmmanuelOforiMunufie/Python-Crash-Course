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
     print("\n" + self.name.title() + " has " + self.cuisine + " available.")
     
     
     
first_restaurant = Restaurant("imperial lotus", "japanese fried rice")
first_restaurant.open_restaurant()

second_restaurant = Restaurant("suncity perking ", "goat meat jollof rice")
second_restaurant.open_restaurant()

third_restaurant = Restaurant("afrikiko", "tuo zaafi")
third_restaurant.open_restaurant()



