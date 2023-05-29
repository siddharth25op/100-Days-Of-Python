# import turtle
#
# squad = turtle.Turtle()
# print(squad)
# squad.shape("turtle")
# squad.color("coral")
# squad.forward(100)
#
# screenm = turtle.Screen()
# print(screenm.canvwidth)
# screenm.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Pokemon", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Charmander", "Fire"])
# print(table)
# table.add_row(["Squirtle", "Water"])

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Pokemon Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)
