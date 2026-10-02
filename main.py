from tkinter import *
# import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
SOURCE_LANGUAGE = "French"
TARGET_LANGUAGE = "English"

# Change the value when in different devices or directories
src_lang_file = "/Users/U077548/Documents/Personal/Study/Python/[Day 31] flash-cards/data/french_words.csv"

# =============== Random word picker ==================== #

def random_word():
    with open(src_lang_file) as lang_file:
        # data = pd.read_csv(lang_file)
        # word_dict = data.to_dict(orient="records")
        # random_word = random.choice(word_dict)[SOURCE_LANGUAGE]
        data = csv.reader(lang_file)
        words = [word[0] for word in data if word[0] != "French"]
        random_word = random.choice(words)
    
    canvas.itemconfig(word_id, text=f"{random_word}")

# =============== Initialize the window =============== #

window = Tk()
window.title("Flashzz")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ==================== Card UI ========================= #
# Load Images
front_card_img = PhotoImage(file="/Users/U077548/Documents/Personal/Study/Python/[Day 31] flash-cards/images/card_front.png")
back_card_img = PhotoImage(file="/Users/U077548/Documents/Personal/Study/Python/[Day 31] flash-cards/images/card_back.png")
check_mark_img = PhotoImage(file="/Users/U077548/Documents/Personal/Study/Python/[Day 31] flash-cards/images/right.png")
cross_mark_img = PhotoImage(file="/Users/U077548/Documents/Personal/Study/Python/[Day 31] flash-cards/images/wrong.png")

# Set up the card background with canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_card_img)
canvas.create_text(400, 150, text=SOURCE_LANGUAGE, font=("Ariel", 40, "italic"))
word_id = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=cross_mark_img, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=check_mark_img, highlightthickness=0, command=random_word)
right_button.grid(row=1, column=1)

# ======================================================= #

window.mainloop()
