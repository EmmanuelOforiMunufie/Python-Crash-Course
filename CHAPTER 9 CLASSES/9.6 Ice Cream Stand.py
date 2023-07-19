class Restaurant():
    """Modelling a restaurant"""
    
    def __init__ (self, name, cuisine):
        """Initialize name and cuisine attributes."""
        self.name = name.title()
        self.cuisine = cuisine
        
    def describe_restaurant(self):
     """Welcome message of restaurant"""   
     print(self.name.title() + " is open and welcomes you" + "\n")
         
    def open_restaurant(self):
     """Display food available """
     print(self.name.title() + " has " + self.cuisine + " available.")

class IceCreamStand(Restaurant):
    """Modelling an Ice cream stand"""
    
    def __init__(self, name, cuisine = "ice cream"):
        """Initialize attributes from Restaurant"""
        super(IceCreamStand,self). __init__( name, cuisine)
        self.flavors = []   
        
    def display_flavors(self):
        """Display flavors available"""
        for flavor in self.flavors:
            print(flavor.title() + " ice cream is availble.")
    
    
    
restaurant_icecream = IceCreamStand("abelewas")
restaurant_icecream.flavors = ["chocolate", "vanilla", "strawberry", "chocolate chip"]

restaurant_icecream.describe_restaurant()
restaurant_icecream.display_flavors()
     