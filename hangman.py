import random
words = ["python", "developmemt", "computer", "malayalam", "program"]
word = random.choice(words)
guessed_letters = []
attempts = 6
display = ["_"] * len(word)
print(" Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have", attempts, "attempts.\n")
while attempts > 0 and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print(" You already guessed that letter")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print(" Correct guess")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(" Wrong guess!")
        print("Remaining attempts:", attempts, " ")
if "_" not in display:
    print(" Congratulations! You guessed the word:", word)
else:
    print(" Game Over! The word was:", word)
