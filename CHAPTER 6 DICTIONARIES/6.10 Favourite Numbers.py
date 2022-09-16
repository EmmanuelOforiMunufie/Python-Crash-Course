favourite_numbers = {"Mac":[300, 250, 360],
                    "Kofi":[3, 99, 950], 
                    "Timo":[4, 10],
                    "Addo":[5, 15, 455, 657, 567],
                    "Karl":[8, 233, 90, 432],
                    }

for name,numbers in favourite_numbers.items():
    print("\n" + name.title() + "'s favourite numbers are:")
    for number in numbers:
        print(number)