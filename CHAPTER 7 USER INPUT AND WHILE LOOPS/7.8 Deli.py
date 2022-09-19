sandwich_orders = ["chicken sandwich" , "egg sandwich" , "seafood sandwich", "roast beef sandwich" , "ham sandwich" , "nutella sandwich"]
finished_sandwiches = []


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("We are making " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)
 
print("\n")   
for sandwich in finished_sandwiches:
    print("I made your " + sandwich + ".")