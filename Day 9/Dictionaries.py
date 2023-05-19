my_dict = {
    "Pokemon": "They are just super natural animals.",
    "Pikachu": "It's a electric type pokemon."
}

#Adding new items to directory
my_dict["Loop"] = "This is a loop."

#create a empty dictionary.
em_dict = {}

#wipe an existing disctionary
#my_dict = {}
#print(my_dict)

#Edit an item in a dictionary.
my_dict["Loop"] = "This is a new Loop."
print(my_dict["Loop"])

#Looping though a dictionary
for key in my_dict:
    print(key)
    print(my_dict[key])