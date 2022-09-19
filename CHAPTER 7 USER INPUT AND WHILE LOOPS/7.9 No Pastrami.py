sandwich_orders = ["chicken sandwich", "pastrami sandwich" , "egg sandwich" , "seafood sandwich", "roast beef sandwich" , "ham sandwich" , "nutella sandwich" , "pastrami sandwich"]   
finished_sandwiches = []
print("We have run out of pastrami sandwich")
print("\n")


while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("We have " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("\n")   
for sandwich in finished_sandwiches:
    print("I made your " + sandwich + ".")