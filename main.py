import os

def wordChecker(secretWordTwo, correctLetter):
  for x in secretWordTwo:
    if x not in correctLetter:
      return False
      



print("Welcome to Hangman!")

playerOne = input("Whats player one's name?\n")
print("Welcome", playerOne)


playerTwo = input("What is the name of the second player?\n")
print("Welcome", playerTwo)

print("Rules of the game")
print(playerOne, "will enter a secret word\n")
print(playerTwo, "will have 6 chances to guess correct letters")

lives = 6 

secretWord = input("Player One enter the secret word\n")
hint = input("What is the topic or genre of the secret word\n")

os.system('clear')

correctLetters = []
incorrectLetters = []

while lives != 0:

  guess = input("Please guess a letter\n")

  if guess == "hint":
    print("The hint is ", hint)
    
  elif guess in secretWord:
    correctLetters.append(guess)
    print("You guessed that letter correctly!")

  elif guess not in secretWord:
    incorrectLetters.append(guess)
    lives = lives - 1
    print("You guessed this letter incorrectly, you now have ", lives, " left")

  elif guess in correctLetters:
    print("You've already guessed this letter. It was correct")

  elif guess in incorrectLetters:
    print("You've already guessed this letter. It was incorrect")

  

  if wordChecker(secretWord, correctLetters) != False:
    print("You got the word right!\n")
    print("You win!")
    break

  

      