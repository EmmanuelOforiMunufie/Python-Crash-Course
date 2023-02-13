def car_info(manufacturer, model,**other_info):
    """Build a dictionary containing information about a car."""
    info = {}
    info["car_manufacturer"] = manufacturer
    info["car_model"] = model
    for key,value in other_info.items():
        info[key]= value
    return info    

car_profile = car_info("mercedes", "gclass",colour="blue black",tow_package="True")
car_profile = car_info("ferrari ", "purosangue",colour="black",turbo_charger="twin",transmission_type="automatic")

print(car_profile)