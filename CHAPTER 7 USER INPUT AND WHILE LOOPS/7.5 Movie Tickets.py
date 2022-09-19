prompt = "How old are you? "
prompt += "\nEnter quit when you are done. " 

while True:
    age = input(prompt)
    age = int(age)
    if age == 'quit':
        break
if age < 3:
    print("free entry for persons below 3")
elif age < 12:
    print("your ticket is $10")
else:
    print("your ticket is $15")
    