ANIMATIONS = {
    1: '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    2: '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    3: '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    4: '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    5: '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    6: '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    7: '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
}

def progress(wordl, correct):
    for c in wordl:
        if c in correct:
            print(c, end=" ")
        else:
            print("_", end=" ")


def wordtoguess():
    print("Please enter the word required to be guessed")
    word=input()
    return word


def animations(lives):
    animation = ANIMATIONS[lives]
    print(animation)

def getletter():
    letter=input("give me a letter\n")
    return letter


correct=set() # initialize the set
lives = 1 # number of starting lives that influences the animation, goes forward and ends at 7
word = wordtoguess() #gets input from user and saves it in word variable

correct.add(word[0]) # shows first letter in the word
correct.add(word[-1]) # shows the second letter in the word
progress(word,correct) # shows the initial game state of the word to guess

while lives != 7:
    animations(lives)
    letter=getletter()

    if letter in word:
        print("Correct!\n")
        correct.add(letter)
    else:
        print("Incorrect\n")
        lives=lives+1

    if all(c in correct for c in word):
        print("you won")
        break

    progress(word, correct)

progress(word, correct)
if lives==7:
    print("You lost")







