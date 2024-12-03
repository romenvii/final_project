# Galactic_Gridlock.py

import pygame 
import random

# Global variables
SCREENWIDTH = 800
SCREENHEIGHT = 800
CELLSIZE = 20
GRIDSIZE = 15
PLAYERGRID = (50, 50)
CPUGRID = (450, 50)
RUN = True
# Color values for white and black
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initializes the pygame modules, and applies the size settings for the display window and caption for the display window
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Galactic Gridlock")

# Sets the screen to white
screen.fill(WHITE)

# This function creates a 15 by 15 grid using the grid position as x and y coordinates for the player grid or the computer grid, allowing the grid to be any where on the screen
def create_grid(gridposition):
    startingX, startingY = gridposition
    for row in range(GRIDSIZE + 1):
        y = startingY + row * CELLSIZE
        pygame.draw.line(screen, BLACK, (startingX, y), (startingX + (GRIDSIZE * CELLSIZE), y))
    for column in range(GRIDSIZE + 1):
        x = startingX + column * CELLSIZE
        pygame.draw.line(screen, BLACK, (x, startingY), (x, startingY + (GRIDSIZE * CELLSIZE)))

# Draws the player and computer grid on the screen
create_grid(PLAYERGRID)
create_grid(CPUGRID)

# Updates the screen so the create grid and screen fill functions can be applied
pygame.display.flip()

def main():
    pass

# Main game loop that exits the game if the X is clicked on the display window
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

# Unitializes all pygame modules
pygame.quit()

if __name__=="__main__":
    main()