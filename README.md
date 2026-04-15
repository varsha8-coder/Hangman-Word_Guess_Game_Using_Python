# Hangman-Word_Guess_Game_Using_Python

This program is a basic implementation of the classic Hangman game using Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time within a limited number of attempts.

At the start, the program displays blank spaces (underscores) representing each letter of the hidden word. The player inputs a letter, and the program checks whether the guessed letter is present in the word. If the guess is correct, the letter is revealed in its correct position(s). If the guess is wrong, the number of remaining attempts decreases.

The game continues until the player either successfully guesses all the letters in the word or runs out of attempts. The program also prevents repeated guesses by notifying the user if a letter has already been entered.

Finally, the program displays a success message if the player wins, or a game-over message along with the correct word if the player loses.
