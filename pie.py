"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import random
import pygame
from random import *
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
s = randrange(20,80)
x = 350 
x_speed = randrange(-10, 10)
y = 250
y_speed = randrange(-10, 10)
color = [(219, 110, 255), (75, 230, 232), (120, 0, 255), (99, 74, 127)]
c = randint(0, len(color)-1)

r = randrange(20,80)
a = 350 
a_speed = randrange(-10, 10)
b = 250
b_speed = randrange(-10, 10)
color = [(219, 110, 255), (75, 230, 232), (120, 0, 255), (99, 74, 127)]
d = randint(0, len(color)-1)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    x = x + x_speed
    y = y + y_speed 
    if x > 700 - s//2:
        x_speed = -10 
    if y > 500 - s//2:
        y_speed = -10
    if x < 0 +  s //2: 
        x_speed = 10 
    if y< 0 + s//2:
        y_speed = 10

    a = a + a_speed
    b = b + b_speed 
    if a > 700 - s//2:
        a_speed = -10 
    if b > 500 - s//2:
        b_speed = -10
    if a < 0 +  s //2: 
        a_speed = 10 
    if b< 0 + s//2:
        b_speed = 10

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    pygame.draw.circle(screen, color[c], (x, y), s, 10)
    pygame.draw.circle(screen, color[d], (a, b), r, 10)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
