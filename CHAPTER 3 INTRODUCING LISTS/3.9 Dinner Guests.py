guest_list = [ ]
guest_list = ["Mac Miller", "Geoff Hinton", "AA Munufie"," Dave Chapelle", "Bill Burr", "Usain Bolt" ]
print("Dear " + guest_list[0] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[1] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[2] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[3] + "," +  "I would like to invite you to dinner.")
print("Dear" +  guest_list[4] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[5] + "," +  "I would like to invite you to dinner.")

print("Hey people, I have found a bigger dinner table")
guest_list.insert(0, "Alhan Gencay" )
guest_list.insert(3, "Leonardo DiCaprio")
guest_list.append("Elon Musk")
print(guest_list)

print("Dear " + guest_list[0] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[1] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[2] + ", " + "I would like to invite you to dinner.")
print("Dear " + guest_list[3] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[4] + "," +  "I would like to invite you to dinner.")
print("Dear" +  guest_list[5] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[6] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[7] + "," +  "I would like to invite you to dinner.")
print("Dear " + guest_list[8] + "," +  "I would like to invite you to dinner.")
print(len(guest_list))
print("\nHey guys unfortunately my dinner table will not be available on time for the dinner and I have space for only two people.Sorry for any inconveniences" )

popped_guest = guest_list.pop()
print("Dear " + guest_list.pop() + "," + "I am sorry our scheduled dinner will not come off as planned " + ".")

popped_guest = guest_list.pop(1)
print("Dear " + guest_list.pop(1) + "," + "I am sorry our scheduled dinner will not come off as planned " + ".")

popped_guest = guest_list.pop(1)
print("Dear " + guest_list.pop(1) + "," + "I am sorry our scheduled dinner will not come off as planned " + ".")

print(guest_list)
last_popped_guest = guest_list.pop()
print("Dear " + last_popped_guest.title() + " ," + " I am sorry our scheduled dinner will not come off as planned " + ".")
print(guest_list)


del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)
