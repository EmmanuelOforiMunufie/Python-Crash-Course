from random import randint
x = randint(1, 6)

class Die:
    """Represent die"""
    
    def __init__(self,side=6):
        """Initialize die"""
        self.side = side
        
    def roll_die(self):
        """Printing a random number between 1 and the number of sides the die has."""
        return randint(1,self.side)

# Make a 6-sided die and roll it 10 times.  
s6 = Die()  

outcomes = []
for roll_num in range(10):
    outcome = s6.roll_die()
    outcomes.append(outcome)
print("10 rolls of 6-sided die:")
print(outcomes)

# Make a 10-sided die, and show the results of 10 rolls.
s10 = Die(side=10)

outcomes = []
for roll_num in range(10):
    outcome = s10.roll_die()
    outcomes.append(outcome)
print("\n10 rolls of a 10-sided die:")
print(outcomes)

# Make a 20-sided die, and show the results of 10 rolls.
s20 = Die(side=20)

outcomes = []
for roll_num in range(10):
    outcome = s20.roll_die()
    outcomes.append(outcome)
print("\n10 rolls of a 20-sided die:")
print(outcomes)
