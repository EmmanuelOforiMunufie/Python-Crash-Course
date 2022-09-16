favourite_places = {
                    "kofi": ["dubai", "ontario", "amsterdam"],
                    "kojo": ["paris", "london", "cairo"],
                    "aba" : ["new york", "los angeles", "toronto"]
                    }

for name,places in favourite_places.items():
    print("\n" + name.title() + "'s favourite places are:")
    for place in places:
        print("\t" + place.title())
    