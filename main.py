import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()     # clock object
testFont = pygame.font.Font("fonts/Pixeltype.ttf", 50)

sky = pygame.image.load("images/Sky.png")
ground = pygame.image.load("images/ground.png")
testSurface = testFont.render("My game", False, "Black")


while True:
    # check all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # closing program without the error

    window.blit(sky, (0, 0))
    window.blit(ground, (0, 300))
    window.blit(testSurface, (300, 50))

    pygame.display.update()
    clock.tick(60)      # maximum frame rate
