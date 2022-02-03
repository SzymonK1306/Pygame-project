import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    window.blit(score_surf, score_rect)
    return current_time

pygame.init()       # initiation pygame
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")    # title of the window
clock = pygame.time.Clock()     # clock object
font = pygame.font.Font("fonts/Pixeltype.ttf", 50)  # font object

game_active = False
start_time = 0
score = 0

sky_surf = pygame.image.load("images/Sky.png").convert()     # convert is for our game run faster

ground_surf = pygame.image.load("images/ground.png").convert()

snail_surf = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

# intro screen
player_stand = pygame.image.load("images/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

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
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        window.blit(sky_surf, (0, 0))
        window.blit(ground_surf, (0, 300))
        score = display_score()

        # snail movement
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

        # collision
        if snail_rect.colliderect(player_rect):     # return 1 when is a collision
            game_active = False
            snail_rect.right = 800
    # game over screen
    else:
        window.fill((94, 129, 162))
        window.blit(player_stand, player_stand_rect)
        window.blit(game_name, game_name_rect)
        if score != 0:
            score_message = font.render(f"Your score: {score}", False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center= (400, 330))
            window.blit(score_message, score_message_rect)
        else:
            window.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)      # maximum frame rate
