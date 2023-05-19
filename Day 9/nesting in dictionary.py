#Nesting
capital = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a dictionary

travel_log = {
    "India": ["Mumbai", "Delhi", "Kolkata", "Indore"]
}

#Nesting Dictionary in a Dictionary
travel2_log = {
    "India": {"visited cities": ["Mumbai", "Delhi", "Kolkata", "Indore"], "total_visits": 4}
}

#Dictionaries inside a list.
travel_log = [{
    "Key": ["List"],
    "Key2": {

    }
}]

#Nesting dictionary in lists
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