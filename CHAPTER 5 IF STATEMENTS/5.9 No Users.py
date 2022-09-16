usernames = []
if usernames ==[]:
    print("We need to find some users!")

for username in usernames:
    if username == "Admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + "," + "thank you for logging in again.")
