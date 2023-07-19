from my_admin import Admin

user_one = Admin("emmanuel", "munufie", "robotics", "sunyani")
user_one.describe_user()


print("\nAdding privileges...")
user_one.privileges = [
    "can start a trend",
    "can take down offensive posts",
    "can moderate conversations "
    ]               


user_one.show_privileges()