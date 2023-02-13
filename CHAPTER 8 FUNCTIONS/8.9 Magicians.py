def show_magicians(magicians):
    """Print names of magicians in the list"""
    for magician in magicians:
        print(magician.title())

magicians= ["david blaine", "harry houdini", "david copperfield", "teller"]
show_magicians(magicians)