def show_magicians(magicians):
    """Print names of magicians in the list"""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Add 'the great' to each magician and move to great_magicians """
    great_magicians = []
    
    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() + ' the Great' 
        great_magicians.append(great_magician)
        
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians= ["david blaine", "harry houdini", "david copperfield", "teller"]
show_magicians(magicians) 

print("\n")       
make_great(magicians)
show_magicians(magicians)

        

    
    
    
    

    
    




