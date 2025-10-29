#import pyqt6
import sys
from random import randint
from rapidfuzz import fuzz 

# from models.Person import Person
from models.Word import Word
# from models.Result import Result

from utilities.Avatar import Avatar
from utilities.Choice import Choice
from utilities.NLP import NLP

from math import *

wordCls = Word()

wordCls.resetWords()


class SpellSmart(Avatar):

    def __init__(self, name="Broomhilda", userSR=True, show=True):

        super().__init__(name, userSR, show)
        self.say(f"Hello! Welcome to spell smart! My name is {self.getName()}. I will help you practice your spelling skills.")
        self.maxWords = 5

    def getWord(self):
        word = Word.getRandomWord()
        self.say(f"Can you spell {word.getWord()}",show = False)
        answer = input('Please spell the word here: ')
        self.spellWord(word, answer)
        if len(answer) > len(word.getWord()):
                self.say("You have put to many letters please try again")
        
   
    def spellWord(self, word, answer=None):
        self.say(f"You spelt the word: {word.getWord()} as follows:", show=False)
        
        for letter in answer:
            self.say(letter.upper())
        
        percentage = fuzz.ratio(word.getWord().upper(), answer.upper())
                
        self.say(f"You got {percentage:.2f}% correct")

        if percentage >= 100.0:
            word.setIsUsed(True)
            word.save()
        # self.say(f"You got {rightLetters} out of {len(word)} letters correct")

    def play(self):
        
        
        # get student 

        # loop spelling until words spelt - e.g max 5 words - add result for each word
        self.wordsSpelt = 0
        wordSpeltCorrect = False
        completedSpelling = False

        while self.wordsSpelt < self.maxWords:
            # get a word
            word = wordCls.getRandomWord()

            attempts = 0
            result = 0
            speltWord = ''
            # loop spelling word until get spelt correct
            if completedSpelling == False:
                self.say(f'Please spell {word}', show=False)
                wordSpeltCorrect == False
            while wordSpeltCorrect == False:
                speltWord = input('Please spell the word here: ')

                if speltWord.lower() == word.lower():
                    self.say('You spelt the word correctly')
                    wordSpeltCorrect == True
                    break
                    # wordCls.save()
                else:
                    rat = floor(fuzz.ratio(word, speltWord))
                    self.say(f'You spelt the word wrong. You got the word {rat} percent correct. Please try again')
                    
                

            # write word and attempts to results table

        # show results


def main():
    game = SpellSmart()
    game.play()

    count = 0

    while count < 5:
        try:
            game.getWord()
        except AttributeError:
            break

        count += 1

if __name__ == "__main__":
    main()
  


