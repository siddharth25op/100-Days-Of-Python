from tkinter import *

window = Tk()
window.title("Miles to Kilometer")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Arial", 20))
my_label.grid(column=2, row=0)

is_equal_to = Label(text="is_equal_to", font=("Arial", 20))
is_equal_to.grid(column=0, row=1)

answer = Label(text="0", font=("Arial", 20))
answer.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 20))
km.grid(column=2, row=1)


def button_clicked():
    final_value = float(miles_input.get()) * 1.609344
    answer.config(text=round(final_value, 2))


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
