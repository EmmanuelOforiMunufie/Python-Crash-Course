pizzas = [
    "cheese pizza",  "pepperoni pizza", 
    "meat pizza",
     ]

friend_pizzas = pizzas[:]
pizzas.append("hawaiin pizza")
friend_pizzas.append("buffalo pizza")

print(pizzas)
print(friend_pizzas)
print("My favourite pizzas are:")

for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")

for friend_pizza in friend_pizzas:
    print(friend_pizza)
