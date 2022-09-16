guest_list = ["Mac Miller", "Geoff Hinton", "AA Munufie"]
print("Dear " + guest_list[0] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[1] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[2] + "," +  "I would like to invite you to dinner.")
print(guest_list[1] + " won't be able to make it to your dinner.")

guest_list = ["Mac Miller", "Geoff Hinton", "AA Munufie"]
del guest_list[1]
guest_list.insert(1, "Michael Jordan")
print("Dear " + guest_list[1] + ", " + "I would like to invite you to dinner.")
print(guest_list)
print("Dear " + guest_list[0] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[1] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[2] + "," +  "I would like to invite you to dinner.")
