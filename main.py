import pygame
from sys import exit

pygame.init()       # initiation pygame
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")    # title of the window
clock = pygame.time.Clock()     # clock object
font = pygame.font.Font("fonts/Pixeltype.ttf", 50)  # font object

sky_surf = pygame.image.load("images/Sky.png").convert()     # convert is for our game run faster

ground_surf = pygame.image.load("images/ground.png").convert()

text_surf = font.render("My game", False, "Black")

snail_surf = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))


while True:
    # check all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # closing program without the error

    window.blit(sky_surf, (0, 0))
    window.blit(ground_surf, (0, 300))
    window.blit(text_surf, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right < -100:
        snail_rect.left = 800

    window.blit(snail_surf, snail_rect)
    window.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)      # maximum frame rate
