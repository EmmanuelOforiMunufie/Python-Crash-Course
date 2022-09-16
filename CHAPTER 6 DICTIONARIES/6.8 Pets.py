

pet_1 = {
        "name": "obinim",
        "type of animal": "dog",
        "owner": "munufie",
       }

pet_2 = {
        "name": "kix",
        "type of animal": "parrot",
        "owner": "bates",
        }

pet_3 = { 
        "name": "nemo",
        "type of animal": "fish",
        "owner": "brit",
        }

pet_4 = {
        "name": "saddie",
        "type of animal": "horse",
        "owner": "owen",
        }
pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print("\npet:" +  pet["name"])
    print("type of animal:" + pet["type of animal"])
    print("owner:" + pet["owner"].title())