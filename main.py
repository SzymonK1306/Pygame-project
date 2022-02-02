import pygame
from sys import exit

pygame.init()       # initiation pygame
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")    # title of the window
clock = pygame.time.Clock()     # clock object
font = pygame.font.Font("fonts/Pixeltype.ttf", 50)  # font object

game_active = True

sky_surf = pygame.image.load("images/Sky.png").convert()     # convert is for our game run faster

ground_surf = pygame.image.load("images/ground.png").convert()

score_surf = font.render("Score:", False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

gravity = 0


while True:
    # check all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # closing program without the error
        if game_active:
            if event.type == pygame.KEYDOWN:        # keyboard input
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:    # checking mouse collision
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 300:
                        gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        window.blit(sky_surf, (0, 0))
        window.blit(ground_surf, (0, 300))
        pygame.draw.rect(window, "#c0e8ec", score_rect)
        window.blit(score_surf, score_rect)

        snail_rect.x -= 4
        if snail_rect.right < -100:
            snail_rect.left = 800

        window.blit(snail_surf, snail_rect)

        # Player
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        window.blit(player_surf, player_rect)


        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     player_rect.bottom = 250
        # else:
        #     player_rect.bottom = 300

        # collision
        if snail_rect.colliderect(player_rect):     # return 1 when is a collision
            game_active = False
            snail_rect.right = 800
    else:
        window.fill("Pink")


    pygame.display.update()
    clock.tick(60)      # maximum frame rate
