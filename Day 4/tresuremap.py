row1 = ["😂","😂","😂"]
row2 = ["😂","😂","😂"]
row3 = ["😂","😂","😂"]
map = [row1, row2, row3]
print("Welcome to tresure map.")
print(f"{row1}\n{row2}\n{row3}")
where_to_put = int(input("Where to put your tresure map? :"))

if where_to_put == 11:
    map[0][0] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 12:
    map[0][1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 13:
    map[0][2] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 21:
    map[1][0] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 22:
    map[1][1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 23:
    map[1][2] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 31:
    map[2][0] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 32:
    map[2][1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
elif where_to_put == 33:
    map[2][2] = "X"
    print(f"{row1}\n{row2}\n{row3}")
else:
    print("Sorry, You put wrong matrix number.")