import random


subjects = [
    "Taylor Swift",
    "Elon Musk",
    "Cristiano Ronaldo",
    "Beyoncé",
    "Tom Cruise",
    "Oprah Winfrey",
    "Bill Gates",
    "Emma Watson",
    "LeBron James",
    "Selena Gomez",
    "Morgan Freeman",
    "Ariana Grande",
    "Dwayne Johnson",
    "Jennifer Lawrence",
    "Shah Rukh Khan"
]

actions = [
    "performed",
    "launched",
    "trained",
    "spoke",
    "donated",
    "filmed",
    "visited",
    "hosted",
    "released",
    "won",
    "designed",
    "sang",
    "wrote",
    "directed",
    "attended"
]

objects = [
    "at Madison Square Garden",
    "to Mars",
    "on the football field",
    "at a charity event",
    "to a children's hospital",
    "in a new action movie",
    "at the United Nations",
    "on a late-night show",
    "a new music album",
    "an Oscar ceremony",
    "a tech conference",
    "in a Broadway musical",
    "on Instagram Live",
    "at a global summit",
    "to his hometown"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)
    
    sentence = f"BREAKING NEWS: {subject} {action} {object}"

    print("\n" + sentence)

    user_input = input("\n do you want another sentence ? (Y/N)").strip().lower()

    if user_input == "n":
        break

print("\nThanks for using this small programe.")

    
