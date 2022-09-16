current_users = ["Kofi", "Kwaku", "Kojo", 
                 "Kwabena", "Yaw", "Kwasi"]

new_users = ["Ameyaw", "Owusu", "kojo",
             "Afriyie", "kwaku"]
current_users = [user.lower() for user in current_users]   #making list case insensitive
for new_user in new_users:
    if new_user in current_users:
        print(new_user + " taken.Please enter a new username.")
    else:
        print(new_user + " is available.")       