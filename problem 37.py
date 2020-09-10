# Moved the ANIMATIONS constant to a different module: animations.py
# Usually constants are kept in a different module to help the code stay clean and small
# See the line below on how to import a variable from another module
from animations import ANIMATIONS


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


# Added a setup function
# Why? Because there was a bulk of code in the "main" function which could be included in the setup function
# This function returns: word, correct (we need them to be used in the next function calls after setup)
def setup():
    correct=set() # initialize the set

    # Commented the line below, see the play function above
    # Read about default arguments in function
    # lives = 1 # number of starting lives that influences the animation, goes forward and ends at 7

    word = wordtoguess() #gets input from user and saves it in word variable

    correct.add(word[0]) # shows first letter in the word
    correct.add(word[-1]) # shows the second letter in the word
    progress(word,correct) # shows the initial game state of the word to guess

    return word, correct

# Moved the rest of the code below the setup phase in this function
# We need to know in this function who <word> and <correct> are, that's why they are the arguments of this function
def play(word, correct):
    lives = 1

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
            print(word)

            # Commented this statement cause its effect was to exit only the current control flow statement
            # In this case it was an "if"
            # break

            # The return statement's effect is that it exits the function immediately
            # The function served its purpose
            return print("You won")

        progress(word, correct)

    # Moved the Lost Game message here
    # This call is made after the while was executed
    # If the player guessed the word, the return statement above woul exit the function
    # So, this line will not be reached
    #
    # The while statements ends when lives == 7
    # So when we are here, the player has lost the game -> print out Lost Game message
    print("You lost")


# It's like the main in c++
# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    word, correct = setup()
    lives = play(word, correct)

    # Redundant call: if you lose, the word is printed 2 times
    # progress(word, correct)

