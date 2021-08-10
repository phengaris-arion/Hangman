import random

class Word:

    def __init__(self):
        words = ("foxglove", "captain", "oxygen", "microwave", "rhubarb")
        self._word = random.choice(words)
        self.letters_in_word=set(self._word)

    @property
    def word(self):
        return self._word

    def progress(self, guesses):
        # create string of underscores and guessed letters to show progress to guessing word
        progress_string= ""
        for char in self.word:
            if guesses.guessed(char):
                progress_string= progress_string+" "+char+" "
            else:
                progress_string= progress_string +" _ "
        return(progress_string)

    def guessed(self, guesses):
        letters_guessed = self.letters_in_word.intersection(guesses.guesses_made)
        if letters_guessed == self.letters_in_word:
            return True
        else:
            return False


class Guesses:

    def __init__(self):
        # guesses holds all guesses made (wrong or right)
        self.guesses_made = set()

    def guessed(self,char):
        if char in self.guesses_made:
            return True
        else:
            return False

    def record(self,guess,word):
        # All valid guesses (wrong or right) are added to the guesses set
        self.guesses_made.add(guess)
        if not guess in word.letters_in_word:
            Gallows.record_bad_guess()

    def made(self):
        # to sort the set of guesses made we need to cast it to a list
        guesses_list= list(self.guesses_made)
        guesses_list.sort()
        guesses_string=""
        #comma separate the guesses
        for char in guesses_list:
            guesses_string= guesses_string+char+","
        return guesses_string

class Gallows:

    _bad_guesses=0

    gallows_images = ("      \n      \n        \n         \n        \n__________",
                      "      \n |    \n |      \n |       \n |      \n_|________",
                      " _____\n |    \n |      \n |       \n |      \n_|________",
                      " _____\n |/   \n |      \n |       \n |      \n_|________",
                      " _____\n |/  |\n |      \n |       \n |      \n_|________",
                      " _____\n |/  |\n |   O  \n |       \n |      \n_|________",
                      " _____\n |/  |\n |   O  \n |   |   \n |      \n_|________",
                      " _____\n |/  |\n |   O  \n |  /|   \n |      \n_|________",
                      " _____\n |/  |\n |   O  \n |  /|\\ \n |      \n_|________",
                      " _____\n |/  |\n |   O  \n |  /|\\ \n |  /   \n_|________",
                      " _____\n |/  |\n |   O  \n |  /|\\ \n |  / \\\n_|________",)

    @classmethod
    def record_bad_guess(cls):
        cls._bad_guesses +=1

    @classmethod
    def hanged(cls):
        if cls._bad_guesses >= len(cls.gallows_images)-1:
            return True
        else:
            return False

    @classmethod
    def draw(cls):
        return cls.gallows_images[cls._bad_guesses]

if __name__ == "__main__":
    target= Word()
    print("hello")
    print(target.word())
