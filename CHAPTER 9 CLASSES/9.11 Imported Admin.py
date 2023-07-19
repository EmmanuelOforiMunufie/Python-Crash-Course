from my_user import Admin
 
emmanuel = Admin("emmanuel", "munufie", "robotics", "sunyani")
emmanuel.describe_user()



emmanuel.privileges = [
    "can start a trend",
    "can take down offensive posts",
    "can moderate conversations "
    ]               

emmanuel.show_privileges() 