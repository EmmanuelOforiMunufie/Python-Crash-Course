teams = ["man united", "golden State warriors", "boston red sox", "arizona cardinals", "seattle sounders", "portland timbers"]
print(teams)
teams[0] = "kansas city chiefs"
print(teams)
teams.append("boston celtics")
print(teams)
teams.insert(2,"miami heat")
print(teams)
del teams[3]
print(teams)
popped_team = teams.pop()
print(teams)
print(popped_team)

popped_team = teams.pop(0)
print ("I am a fan of " + popped_team)

teams.remove("portland timbers")
print(teams)

won_a_championship = "seattle sounders"
teams.remove(won_a_championship)
print(teams)
print("\nThe " + won_a_championship.title() + " won a championship last year " + ".")

teams.sort()
print(teams)
teams.sort(reverse = True)
print(teams)

teams = ['miami heat', 'golden State warriors', 'arizona cardinals']
print(sorted(teams))
print(teams)

teams.reverse()
print(teams)

print(len(teams))