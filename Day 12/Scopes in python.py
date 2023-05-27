pokemon = 5

def new_pokemon():
    pokemon = 10
    print(pokemon)

new_pokemon()
print(pokemon)

##Local Scope##
#def pikachu():
#    pika = 1
#    print(pika)

#pikachu()
#print(pika)

##Global Scope##
Ditto = 58

def new():
    print(Ditto)

new()
print(Ditto)