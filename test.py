import sys
import pygame
from spellSmart import SpellSmart

pygame.init()

# Screen setup
SW = 800
SH = 500
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Spellsmart")

# Load background
background = pygame.image.load("images/home.png")

# Font
font = pygame.font.Font(None, 40)

# --- Text box setup ---
input_boxes = [
    pygame.Rect(200, 180, 500, 50),  # Box 1 position/size
    pygame.Rect(200, 300, 500, 50)   # Box 2 position/size
]

colors = {
    "inactive": pygame.Color("gray70"),
    "active": pygame.Color("dodgerblue2")
}

active_box = None
texts = ["", ""]  # Stores text for each box

# --- Main loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse clicked inside a text box
            active_box = None
            for i, box in enumerate(input_boxes):
                if box.collidepoint(event.pos):
                    active_box = i
                    break

        elif event.type == pygame.KEYDOWN and active_box is not None:
            if event.key == pygame.K_RETURN:
                print(f"Box {active_box + 1} input:", texts[active_box])
                texts[active_box] = ""
            elif event.key == pygame.K_BACKSPACE:
                texts[active_box] = texts[active_box][:-1]
            else:
                texts[active_box] += event.unicode

    # --- Drawing ---
    screen.fill("white")
    screen.blit(background, (0, 0))

    for i, box in enumerate(input_boxes):
        # Draw box
        color = colors["active"] if active_box == i else colors["inactive"]
        pygame.draw.rect(screen, color, box, 2)

        # Render text
        txt_surface = font.render(texts[i], True, pygame.Color("black"))
        screen.blit(txt_surface, (box.x + 10, box.y + 10))

    pygame.display.flip()
