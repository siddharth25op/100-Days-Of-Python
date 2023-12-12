from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def genpassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(0, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwordInput.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def data():
    website = websiteInput.get()
    email = emailInput.get()
    password = passwordInput.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not website or not email or not password:
        messagebox.showinfo(title="Invalid Entry", message="Empty entry not allowed")
    else:
        is_ok = messagebox.askokcancel(title="Confirm", message="Are you sure you want to save these info?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    #Reading old data
                    hui = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                hui.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(hui, file, indent=4)
            finally:
                websiteInput.delete(0, END)
                passwordInput.delete(0, END)
                emailInput.delete(0, END)
######################################################################


def searchdata():
    website = websiteInput.get()
    email = emailInput.get()
    try:
        with open("data.json", "r") as file:
            poke = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Result", message="There is no data file.")
    else:
        if not website or not email:
            messagebox.showinfo(title="Invalid Entry", message="Empty entry not allowed")
        elif email == poke.get(f"{website}", {}).get("email"):
            password = poke[website]["password"]
            messagebox.showinfo(title="Details", message=f"website: {website}\nemail: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Result", message="Email associated with the website not found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)
emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=2, column=0)
passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3, column=0)

websiteInput = Entry(width=45)
websiteInput.grid(row=1, column=1, columnspan=2)
websiteInput.focus()
emailInput = Entry(width=45)
emailInput.grid(row=2, column=1, columnspan=2)
passwordInput = Entry(width=26)
passwordInput.grid(row=3, column=1)

genPass = Button(text="Generate Password", command=genpassword)
genPass.grid(row=3, column=2)

addButton = Button(text="Add", width=38, command=data)
addButton.grid(row=4, column=1, columnspan=2)

searchButton = Button(text="Search Data", command=searchdata)
searchButton.grid(row=1, column=2)

window.mainloop()
