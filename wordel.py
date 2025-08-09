


class Wordle:

  MAX_ATTEMPTS = 6
  WORD_LENGTH = 5
  

  def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []

  def check_guess(self, guess: str):
    guess = guess
    color = ["gray"] * 5
    inWord = [False] * 5

   # correct letters in correct positions (green)
    for i in range(5):
        if guess[i] == self.secret[i]:
            color[i] = "green"
            inWord[i] = True

    #  correct letters in wrong positions (yellow)
    for i in range(5):
        if color[i] == "green":
            continue
        for j in range(5):
            if not inWord[j] and guess[i] == self.secret[j]:
                color[i] = "yellow"
                inWord[j] = True
                break

    self.attempts.append((guess, color))
    return color
  
  def last_guess(self):#to store last guess
    return self.attempts[-1][0]
  
  def win(self, guess: str):
        return guess == self.secret
  
  def is_game_over(self):
        return len(self.attempts) >= 6 or (self.last_guess() == self.secret )