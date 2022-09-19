responses = {}
polling_active = True

while polling_active:
    #Ask for person's name and response
    name = input("\nWhat is your name?")
    response = input("What is your dream vacation destination?")
    
    #Store the response in dictionary
    responses[name] = response
    
    # Allow the nomination of other people to take poll
    nominate = input ("Would you like to nominate another person to take this poll? (yes/no)") 
    if nominate == "no":
        polling_active = False
        
    #Polling is complete. Show the results.
    print("\n---Poll Reslts---")
    for name, response in responses.items():
        print(name + " your dream vacation destination is " + response + ".")
    
        