#import pyqt6
import sys
from random import randint

# from models.Person import Person
#from models.Word import Word
# from models.Result import Result

from utilities.Avatar import Avatar
from utilities.Choice import Choice
from utilities.NLP import NLP

class SpellSmart(Avatar):

    def __init__(self, name="Broomhilda", userSR=True, show=True):

        super().__init__(name, userSR, show)
        self.say(f"Hello! Welcome to spell smart! My name is {self.getName()}. I will help you practice your spelling skills.")

    def getWord(self):
        words = ["banana", "apple", "grape", "orange", "melon", "pineapple"]
        word = words[randint(0, len(words) - 1)]
        self.say(f"Can you spell {word}",show = False)
        answer = input('Please spell the word here: ')
        self.spellWord(word, answer)
       
   
   
   
    def spellWord(self, word, answer=None):
        self.say(f"You spelt the word: {word} as follows:")
        rightLetters = 0
        for letter in answer:
            self.say(letter.upper())
        for i in range(len(answer)):
            if word[i].upper() == answer[i].upper():
                rightLetters +=1
        self.say(f"You got {rightLetters} out of {len(word)} letters correct")

   

def test():
    game = SpellSmart()
    game.getWord()
   
if __name__ == "__main__":
    test()
