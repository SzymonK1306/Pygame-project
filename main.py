import pygame
from sys import exit

pygame.init()       # initiation pygame
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")    # title of the window
clock = pygame.time.Clock()     # clock object
font = pygame.font.Font("fonts/Pixeltype.ttf", 50)  # font object

sky_surface = pygame.image.load("images/Sky.png").convert()     # convert is for our game run faster
ground_surface = pygame.image.load("images/ground.png").convert()
textSurface = font.render("My game", False, "Black")
snail_surface = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_xPos = 700



while True:
    # check all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # closing program without the error

    window.blit(sky_surface, (0, 0))
    window.blit(ground_surface, (0, 300))
    window.blit(textSurface, (300, 50))
    snail_xPos -= 4
    if snail_xPos < -100:
        snail_xPos = 700
    window.blit(snail_surface, (snail_xPos, 265))

    pygame.display.update()
    clock.tick(60)      # maximum frame rate
