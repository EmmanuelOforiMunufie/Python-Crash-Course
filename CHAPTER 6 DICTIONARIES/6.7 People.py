person_0 = {"first_name": "Emmanuel",
          "last_name": "Munufie", "city": "Sunyani"}

person_1 = {"first_name" : "Jesse",
           "last_name": "Munufie", "city": "Sunyani"}

person_2 = {"first_name" : "Owusu",
           "last_name": "Munufie", "city": "Sunyani"}

people = [person_0, person_1, person_2]          

for person in people:
    print("\nfirst_name:" + person["first_name"])
    print("last_name:" + person["last_name"])
    print("city:" + person["city"].title())

