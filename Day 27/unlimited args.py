# def add(*args):
#     su = sum(args)
#     print(su)
#
# add(10, 10, 10)

def calc(**kwargs):
    print(kwargs)

calc(add=3, mul=5)

# class Car:
#     def __init__(self, **ania):
#         self.make = ania.get("make")
#         self.model = ania.get("model")
#         self.color = ania.get("color")
#         self.seats = ania.get("seats")
#
# lambo = Car(make="Nichirin", model="GT-R", color="Black", seats=2)
# print(lambo.model, lambo.seats)
