travel2_log = [
    {
        "Country": "India",
        "cities_visited": ["Mumbai", "Delhi", "Kolkata", "Indore"],
        "total_visits": 4 
    },
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon", "Turkey"],
        "total_visits": 4
    }
]

def add_new_country(Country, total_visits, cities_visited):
    new_country = {}
    new_country["Country"] = Country
    new_country["total_visits"] = total_visits
    new_country["cities_vitied"] = cities_visited
    travel2_log.append(new_country)

add_new_country("USA", 2, ["New York", "Los Angelas"])
print(travel2_log)