import hangman

def get_letter(guesses):
    while True:
        char= input("\nPlease enter your guess: ")
        if len(char)<1:
            print ("You didn't choose a letter!")
        elif len(char)!=1:
            print ("One letter at a time!")
        elif not char.isalpha():
            print ("Alphabetic characters only!")
        elif guesses.guessed (char):
            print ("You already guessed that letter")
        else:
            break
    return (char)

def play_game():
    target= hangman.Word()
    guesses= hangman.Guesses()
    gallows=hangman.Gallows()
    while True:
        guess= get_letter(guesses)
        guesses.record(guess,target)
        print("\n",target.progress(guesses))
        print(gallows.draw())
        print("\nUsed: \n",guesses.made())
        if target.guessed(guesses):
            print("\nYou win, well done")
            break
        if gallows.hanged():
            print ("\nI win. The word was:",target.word)
            break

if __name__ == "__main__":
    play_game()
