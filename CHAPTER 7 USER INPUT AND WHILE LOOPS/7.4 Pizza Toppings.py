prompt = "\nPlease enter the pizza toppings you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    pizza_topping = input(prompt)
    
    if pizza_topping == 'quit':
        break
    else:
        print("Adding " + pizza_topping + " to pizza " )
