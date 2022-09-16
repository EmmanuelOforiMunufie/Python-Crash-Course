cities = {
    "toronto" : {
        "country":  "canada",
        "population": "6197000",
        "fact": "Yonge Street in Toronto is the longest street in the world, according to the Guinness Book of World Records. It's 1,896 km long",
        },




    "sunyani" : {
        "country": "ghana",
        "population": "208496",
        "fact": " The British set up a district headquarters there in 1924",
        },




    "montreal": {
        "country": "canada",
        "population":  "1942247",
        "fact": "Montreal is the second largest French speaking citiy in the world, after Paris",
        }
    }
         


for city,city_info in cities.items():
    country = city_info["country"].title()
    population = city_info["population"]
    fact = city_info["fact"]



    print("\ncountry:" + city_info["country"].title())
    print("population:" + city_info["population"])
    print("fact:" + city_info["fact"])
