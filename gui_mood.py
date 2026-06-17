import json
import tkinter as tk
import random
from datetime import datetime

DEFAULT_MOODS = {

    "sleepy": ["go take a nap"],
    "happy": ["yay! keep it up", "stay like this always :)", "that's nice to hear..", "awwiee, letss goo!"],
    "sad": ["it's okay, you'll get over it..", "this will pass too", "nothing is forever..", "its okay not to be okayy", "eat some chocolate ;)"],
    "moody": ["listen to some music!", "take some alone time", "take a nap", "go watch funny cat videos haha"],
    "angry": ["go do cardio for 20 mins!", "breathe, don't react immediately", "grab your fav snack", "go take a walk outside"],
    "hungry": ["go eat something good!", "food first, everything else later", "try out that new recipe in your saved list!"],
    "tired": ["go take a nap, you deserve it ;)"],

    "overthinking": [
        "you're thinking too much, slow down",
        "not everything needs a conclusion right now",
        "take a deep breath and let it out"
    ],

    "annoyed": [
        "ugh, that's irritating huh",
        "take a small break before you explode 😭",
        "don't let one thing ruin your whole day",
        "maybe some music will help"
    ],

    "uneasy": [
        "something feels off huh?",
        "it's okay to not feel settled sometimes",
        "slow down a little, you're safe",
        "take a deep breath first"
    ],

    "not bad": [
        "okayyy we like stable moods 😌",
        "not bad is still better than terrible",
        "glad things aren't too heavy rn",
        "we're surviving and that's enough sometimes"
    ],

    "okay": [
        "just okay? that's valid too",
        "you don't always have to feel amazing",
        "an okay day is still a day you made it through",
        "hope your day gets softer from here :)"
    ]
}

try:
    with open(r"F:\mood_app\moods.json", "r") as file:
        moods = DEFAULT_MOODS.copy()
        moods.update(json.load(file))

except:
    moods = DEFAULT_MOODS.copy()
def set_mood(mood):
    entry.delete(0, tk.END)
    entry.insert(0, mood)

def clear_placeholder(event):
    if entry.get() == "type your mood...":
        entry.delete(0, tk.END)
        entry.config(fg=TEXT)

def add_placeholder(event):
    if entry.get() == "":
        entry.insert(0, "type your mood...")
        entry.config(fg="gray")

def clear_all():
    entry.delete(0, tk.END)
    teach_entry.delete(0, tk.END)

    result.config(text="")

    entry.insert(0, "type your mood...")
    entry.config(fg="gray")

    check_mood()

def check_mood():
    feeling = entry.get().strip().lower()

    if feeling == "":
        result.config(text="type first sillyy")

    elif feeling in moods:

        current_time = datetime.now().strftime("%I:%M %p")

        response = random.choice(moods[feeling])

        result.config(
            text=f"{response}\n\nchecked at {current_time} 🌷"
        )

    else:
        new_reply = teach_entry.get()

        if new_reply == "":
            result.config(text="teach me what to say 😭")

        else:
            moods[feeling] = [new_reply]
            with open(r"F:\mood_app\moods.json", "w") as file:
                json.dump(moods, file)

            result.config(text="YAY i learned a new mood 😎")

            teach_entry.delete(0, tk.END)
            entry.delete(0, tk.END)

BG = "#fff0f5"
BUTTON = "#ffcad4"
TEXT = "#5c374c"
ENTRY = "#ffffff"
ACCENT = "#ffc2d1"

hour = datetime.now().hour

if hour < 12:
    greeting = "good morning 🌷"

elif hour < 18:
    greeting = "good afternoon ☀️"

else:
    greeting = "good evening 🌙"

# Window
window = tk.Tk()
window.title("mood app~")
window.geometry("500x500")
window.configure(bg=BG)

# Title
title = tk.Label(
    window,
    text=f"{greeting}\nHow are you feeling today? 🌷",
    font=("Poppins", 20, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(pady=20)

# Input box
entry = tk.Entry(
    window,
    width=22,
    font=("Poppins", 12),
    justify="center",
    bg=ENTRY,
    fg=TEXT,
    bd=0
    
)

entry.pack(pady=15, ipady=8)
entry.insert(0,"type your mood...")
entry.config(fg="gray")
entry.bind("<Return>", lambda event: check_mood())
entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", add_placeholder)

teach_label = tk.Label(
    window,
    text="teach me a response for unknown moods 👀",
    font=("Poppins", 10)
)

teach_label.pack()
teach_entry = tk.Entry(
    window,
    width=25,
    font=("Poppins", 11),
    justify="center"
)

teach_entry.pack(pady=5, ipady=3)

button_frame = tk.Frame(window, bg=BG)
button_frame.pack(pady=10)

# Button
button = tk.Button(
    button_frame,
    text="check mood!",
    font=("Poppins", 10),
    bd=0,
    cursor="hand2",
    bg=BUTTON,
    fg=TEXT,
    activebackground=ACCENT,
    activeforeground=TEXT,
    relief="flat",
    command=check_mood,
    padx=15,
    pady=5,
)
button.pack(pady=10)

# Result text
result = tk.Label(
    window,
    text="",
    font=("Poppins", 12),
    bg=BG,
    fg=TEXT,
    wraplength=350,
    justify="center"
)

result.pack(pady=20)

# Run app
window.mainloop()