
import os
print("Running from:", os.getcwd())
import json
import random
from datetime import datetime

# Load existing moods or create default ones
try:
    with open("moods.json", "r") as file:
        moods = json.load(file)
except:
    moods = {
        "happy": ["yay! keep it up", "stay like this always :)"],
        "sad": ["it's okay, you'll get over it", "this will pass too"],
        "moody": ["listen to some music!", "take some alone time"],
        "angry": ["go do cardio for 20 mins!", "breathe, don't react immediately"],
        "hungry": ["go eat something good!", "food first, everything else later"],
        "tired": ["go take a nap, you deserve it ;)"],
        "overthinking": [
            "you're thinking too much, slow down",
            "not everything needs a conclusion right now",
            "take a deep breath and let it out"
        ]
    }

while True:
    f = input("how are you feeling? (type 'exit' to quit) ").lower()

    time_now = datetime.now()

    with open("history.txt", "a") as history:
        history.write(f"{time_now} - {f}\n")

    if f == "exit":
        print("bye :)")
        break

    if f in moods:
        print(random.choice(moods[f]))
    else:
        new = input("i don't know this mood... want to teach me? (yes/no) ").lower()

        if new == "yes":
            response = input("what should i say when you feel this? ")
            moods[f] = [response]

            with open("moods.json", "w") as file:
                json.dump(moods, file)

            print("got it. i'll remember this next time!")
            print(random.choice(moods[f]))
        else:
            print("okay, maybe next time.")
