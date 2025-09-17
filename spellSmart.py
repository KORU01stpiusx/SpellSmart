import pygame
import sys


from models.Person import Person
from models.Word import Word
from models.Result import Result

from utilities.Avatar import Avatar
from utilities.Choice import Choice
from utilities.NLP import NLP

class SpellSmart(Avatar):


    def __init__(self, name="Broomhilda", userSR=True, show=True, vix=0):

        super().__init__(name, userSR, show, vix)
        self.say(f"Hello! Welcome to spell smart! My name is {self.getName()}. I will help you practice your spelling skills.")

    def spellWord(self,word=None):
        self.say(f"You spelt the word: {word} as follows:")
        for letter in word:
            self.say(letter)

    def test():
        game = SpellSmart()
        game.spellWord("elephant")


    if __name__ == "__main__":
        test()