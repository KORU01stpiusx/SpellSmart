#import pyqt6
import sys
from random import randint
from rapidfuzz import fuzz 

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
        if len(answer) > len(word):
                self.say("You have put to many letters please try again")
        
       
   
   
   
    def spellWord(self, word, answer=None):
        self.say(f"You spelt the word: {word} as follows:")
        
        for letter in answer:
            self.say(letter.upper())
        
        percentage = fuzz.ratio(word.upper(), answer.upper())
                
        self.say(f"You got {percentage:.2f}% correct")
        # self.say(f"You got {rightLetters} out of {len(word)} letters correct")

   

def test():
    game = SpellSmart()
    game.getWord()
   
if __name__ == "__main__":
    test()
