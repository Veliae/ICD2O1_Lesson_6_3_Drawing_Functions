import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tree")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
# Colors
white = (255, 255, 255)
brown = (82, 29, 0)
dark_green = (15, 82, 0)

# ---------------------------

# ---------------------------
# Functions

# ---------------------------


# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here

    # ----- DRAWING -----
    screen.fill(white)  # always the first drawing command

    # Draw a Tree
    # Trunk
    pygame.draw.rect(screen, brown, [325, 300, 50, 100])

    # Pines (top to bottom)
    pygame.draw.polygon(screen, dark_green, [[350, 120], [300, 200], [400, 200]])
    pygame.draw.polygon(screen, dark_green, [[350, 160], [280, 260], [420, 260]])
    pygame.draw.polygon(screen, dark_green, [[350, 200], [260, 320], [440, 320]])

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
