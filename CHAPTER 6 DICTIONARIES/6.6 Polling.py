favourite_languages = {
                       "jen": "python",
                       "sarah": "c",
                       "edward": "ruby",
                        "phil": "python"
                        }

for name, language in favourite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print("\n")

people = ["jen","sarah","phil","kofi","kojo","kwabena"]
for person in people:
    if person in favourite_languages.keys():
        print( person.title() + " Thank you for taking our poll.")        
    else:
        print(person.title() + " Can you please take our poll?")    