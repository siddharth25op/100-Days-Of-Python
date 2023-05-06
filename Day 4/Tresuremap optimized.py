row1 = ["😂","😂","😂"]
row2 = ["😂","😂","😂"]
row3 = ["😂","😂","😂"]
map = [row1, row2, row3]
print("Welcome to tresure map.")
print(f"{row1}\n{row2}\n{row3}")
where_to_put = input("Where to put your tresure map? :")

row = int(where_to_put[0])
coloumn = int(where_to_put[1])

selected_row = map[row - 1]
selected_row[coloumn - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")