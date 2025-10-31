from random import randint
from math import *

from models.Database import Database

from utilities.Avatar import Avatar
from utilities.NLP import NLP

from rapidfuzz import fuzz

import threading  

import pygame

class loginFunc(Avatar):

    def __init__(self, name="Broomhilda", userSR=True, show=True, vix=1):
        super().__init__(name, userSR, show, vix)
        self.speechLock = threading.Lock()
        self.speaking = False
        self.person = None
        self.firstName = ''

    def askForName(self):
        nlp = NLP()
        cont = False
        while cont == False:
            name = self.listen("Please tell me your first name", useSR = True, show=True)
            nlpName = nlp.getNameByPartsOfSpeech(name)
            correct = self.listen(f"You said your name was: {nlpName}. Is this correct?", useSR = True)
            percent = fuzz.partial_ratio('Yes, correct', correct)
            if percent < 70:
                cont = False
            else:
                self.firstName = nlpName.lower()
                print(self.firstName)
                cont = True

    def findUsername(self):
        db = Database('Game.db')
        result = db.query("SELECT userName FROM persons WHERE LOWER(firstName) = ?;", (self.firstName,))
        if result:
            self.say(f"Welcome back {result[0]["userName"]}")
            self.person = result[0]["userName"]
            return self.person
        else:
            self.say("No user found.")

if __name__ == "__main__":
    NEWLOGIN = loginFunc()
    NEWLOGIN.askForName()
    NEWLOGIN.findUsername()