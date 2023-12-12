import random
import time
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
curCard = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    origional_data = pandas.read_csv("french_words.csv")
    dataDict = origional_data.to_dict(orient="records")
else:
    dataDict = data.to_dict(orient='records')


# ----------------------------##------page setup-----------------##--------------------------------------------##---------


def randomword():
    global curCard, flipTimer
    window.after_cancel(flipTimer)
    curCard = random.choice(dataDict)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{curCard["French"]}", fill="black")
    canvas.itemconfig(cardBg, image=front_img)
    flipTimer = window.after(3000, func=flipcard)


def flipcard():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{curCard["English"]}", fill="white")
    canvas.itemconfig(cardBg, image=back_img)


def known():
    dataDict.remove(curCard)
    print(len(dataDict))
    wlearn = pandas.DataFrame(dataDict)
    wlearn.to_csv("words_to_learn.csv", index=False)
    randomword()


# ----------------------------##------UI Setup-----------------##--------------------------------------------##---------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, func=flipcard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
cardBg = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 130, text="Title", fill="black", font=(FONT_NAME, 30, "bold"))
word_text = canvas.create_text(400, 250, text="Word", fill="black", font=(FONT_NAME, 50, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

wrong_img = PhotoImage(file="wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, highlightthickness=0, command=randomword)
wrong_btn.grid(row=1, column=0, columnspan=2)

right_img = PhotoImage(file="right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, highlightthickness=0, command=known)
right_btn.grid(row=1, column=2, columnspan=2)
randomword()
window.mainloop()
