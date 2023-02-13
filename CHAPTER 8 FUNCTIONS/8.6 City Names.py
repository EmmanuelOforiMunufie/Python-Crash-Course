def city_country(city_name, country_name):
   """Return a string of city and country"""
   return(city_name.title() + ", "   + country_name.title())

city = city_country("accra", "ghana")
print(city)

city = city_country("lome", "togo")
print(city)

city = city_country("cape town", "south africa")
print(city)
