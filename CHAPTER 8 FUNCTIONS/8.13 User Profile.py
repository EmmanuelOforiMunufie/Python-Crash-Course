def build_profile(first, last, **user_info):
    """Build a dictionary containing information about myself."""
    profile = {}
    profile['first_name']= first          
    profile['last_name']= last
    for key,value in user_info.items():   
        profile[key]= value
    return profile

user_profile = build_profile('emmanuel', 'munufie',
                             location='sunyani technical university',
                             field='robotics',
                             height='6 ft 2',
                             age = '29',
                             sex= 'male')

print(user_profile)   
