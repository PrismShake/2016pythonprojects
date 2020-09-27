import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (225, 41 ,124)

pygame.init()

# Set the width and height of the screen [width, height]
length = 700
width = 600
size = (length, width)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Run of Infringement")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
   # --- Main event loop
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

   # --- Game logic should go here
   y=0
   n=0
   if pygame.key.get_pressed()[pygame.K_y]!=0:
       y=1
   elif pygame.key.get_pressed()[pygame.K_n]!=0:
       n=1
   elif pygame.key.get_pressed()[pygame.K_i]!=0:
       i=1
   elif pygame.key.get_pressed()[pygame.K_1]!=0:
       print("Stealth")
   elif pygame.key.get_pressed()[pygame.K_2]!=0:
       print("Strength")
   elif pygame.key.get_pressed()[pygame.K_3]!=0:
       print("Magic")
   elif pygame.key.get_pressed()[pygame.K_4]!=0:
       print("Manipulation")
   elif pygame.key.get_pressed()[pygame.K_x]!=0:
       exit()
   else:
       print("")
   # --- Screen-clearing code goes here

   # Here, we clear the screen to white. Don't put other drawing commands
   # above this, or they will be erased with this command.

   # If you want a background image, replace this clear with blit'ing the
   # background image.
   screen.fill(BLACK)

   # --- Drawing code should go here\
   pygame.draw.rect(screen, GREEN, (20, 20, 660, 360), 0)
   pygame.draw.rect(screen, WHITE, (25, 25, 650, 350), 0)
   pygame.draw.rect(screen, GREEN, (20, 420, 660, 160), 0)
   pygame.draw.rect(screen, BLACK, (25, 425, 650, 150), 0)
   hp_start=pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 150), 0)#the starting HP
   hp_75=pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 112), 0)# the HP -25
   hp_50=pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 74), 0) # the HP -50
   hp_25=pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 36), 0) # the HP -75
   hp_0=pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 1), 0) # the HP -100
   myfont = pygame.font.SysFont("monospace", 25)
   label = myfont.render("HP", 1, WHITE)
   screen.blit(label, (635, 425))

   def text_1(words):
       myfont = pygame.font.SysFont("monospace", 15)
       label = myfont.render(words, 1, WHITE)
       screen.blit(label, (25, 425))

   def text_2(words):
       myfont = pygame.font.SysFont("monospace", 15)
       label = myfont.render(words, 1, WHITE)
       screen.blit(label, (25, 445))

   def text_3(words):
       myfont = pygame.font.SysFont("monospace", 15)
       label = myfont.render(words, 1, WHITE)
       screen.blit(label, (25, 465))

   def text_4(words):
       myfont = pygame.font.SysFont("monospace", 15)
       label = myfont.render(words, 1, WHITE)
       screen.blit(label, (25, 485))

   def text_5(words):
       myfont = pygame.font.SysFont("monospace", 15)
       label = myfont.render(words, 1, WHITE)
       screen.blit(label, (25, 505))

   def question(words):
       myfont = pygame.font.SysFont("monospace", 15)
       label = myfont.render(words, 1, WHITE)
       screen.blit(label, (25, 555))

   text_1("You are walking through the woods and you stumble on and rock and ")
   text_2("YOU DIE!")
   text_3("THE END")
   text_4("YOU LOSE")
   text_5("TOUGH")
   question("YES OR NO (Y/N)")
   pygame.display.flip()
   # --- Go ahead and update the screen with what we've drawn.
   # pygame.display.flip()

   # --- Limit to 60 frames per second
   clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
