import random

# Easy words
easy = [
    "cat", "dog", "sun", "tree", "book",
    "fish", "ball", "home", "cake", "milk"
]

# Medium words
medium = [
    "apple", "river", "mountain", "puzzle", "guitar",
    "ocean", "forest", "bridge", "planet", "rocket"
]

# Hard words
hard = [
    "xylophone", "quarantine", "pneumonia", "rhythm", "zucchini",
    "labyrinth", "juxtapose", "ephemeral", "serendipity", "onomatopoeia"
]

print("Welcome to Magic Word Finding Game")
print("Please enter level: easy(e), medium(m) or hard(h)")

level = input("Enter difficulty level: ").lower()

if level == "e":
    secret = random.choice(easy)
elif level == "m":
    secret = random.choice(medium)
elif level == "h":
    secret = random.choice(hard)
else:
    print("Invalid selection, defaulting to easy level")
    secret = random.choice(easy)

attempts = 0
print("\nGuess the magic word:")
print("Type 'exit' at any time to quit.")  # New instruction

while True:
    guess = input("\nEnter your guess: ").lower()
    
    if guess == "exit":  # New quit feature
        print("Game quit by user. The magic word was:", secret)
        break
    
    attempts += 1

    if guess == secret:
        print(f"Congrats! You found the magic word in {attempts} attempts!")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "*"

    print("Hint:", hint)

print("GAME OVER")