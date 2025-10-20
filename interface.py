#import pyqt6
import sys
from random import randint
import pygame
from spellSmart import SpellSmart

# from models.Person import Person
#from models.Word import Word
# from models.Result import Result

# from utilities.Avatar import Avatar
# from utilities.Choice import Choice
# from utilities.NLP import NLP

pygame.init()

game = SpellSmart()

SW = 800
SH = 500

screen = pygame.display.set_mode((SW,SH))
pygame.display.set_caption("Spellsmart")


background = pygame.image.load("images/home.png")

font = pygame.font.Font(None, 40)

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw background
    screen.fill('white')
    screen.blit(background, (0, 0))
    
    
    
    pygame.display.flip()