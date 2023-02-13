def make_shirt(shirt_size, shirt_design ):
    """Display information about shirt"""
    print("\nThe shirt size is " + shirt_size + ".")
    print("The message on the shirt is :" + shirt_design)

#Using positional arguments    
make_shirt("Large","Every little thing is gonna be alright")     

#Using keyword arguments   
make_shirt(shirt_design="Water will eventually find its level",shirt_size="Extra Large")