This is a simple Wordle game implemented in Python using a gui with Tkinter.
The player has six attempts to guess a randomly chosen 5-letter word. 
After each guess, feedback is given using color codes: green:correct letter in correct position
                                                       orange:correct letter in wrong position 
                                                       black: the word doesnt have this letter
this project has 2 classes, the first class -wordel.py- has most of the game logic. where the second class contains the gui of the game.
the GUI displays a 6x5 grid to track guesses and uses an input field and submit button for interaction. 
The game ends when the player either guesses the word correctly or runs out of attempts.
at the begining i was taking a different route but it would've been harder to implement it using a gui, as it was aiming that the interaction would be through the terminal
