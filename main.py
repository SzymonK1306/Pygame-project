import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
        player_walk2 = pygame.image.load("images/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load("images/player/jump.png").convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fly":
            fly_frame1 = pygame.image.load("images/Fly/Fly1.png").convert_alpha()
            fly_frame2 = pygame.image.load("images/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            snail_frame1 = pygame.image.load("images/snail/snail1.png").convert_alpha()
            snail_frame2 = pygame.image.load("images/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.animation()
        self.rect.x -= 5
        self.destroy()


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    window.blit(score_surf, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):  # obstacle won't be killed
        obstacle_group.empty()
        return False
    return True


pygame.init()  # initiation pygame
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")  # title of the window
clock = pygame.time.Clock()  # clock object
font = pygame.font.Font("fonts/Pixeltype.ttf", 50)  # font object

game_active = False
start_time = 0
score = 0

sky_surf = pygame.image.load("images/Sky.png").convert()  # convert is for our game run faster

ground_surf = pygame.image.load("images/ground.png").convert()

# Obstacles
obstacle_group = pygame.sprite.Group()

# Player
player = pygame.sprite.GroupSingle()    # Create group
player.add(Player())            # which contains sprite

# intro screen
player_stand = pygame.image.load("images/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True:
    # check all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # closing program without the error
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail"])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        window.blit(sky_surf, (0, 0))
        window.blit(ground_surf, (0, 300))
        score = display_score()

        # Player
        player.draw(window)
        player.update()
        # Obstacles
        obstacle_group.draw(window)
        obstacle_group.update()

        game_active = collision_sprite()

    # game over screen
    else:
        window.fill((94, 129, 162))
        window.blit(player_stand, player_stand_rect)
        window.blit(game_name, game_name_rect)
        gravity = 0
        if score != 0:
            score_message = font.render(f"Your score: {score}", False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 330))
            window.blit(score_message, score_message_rect)
        else:
            window.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)  # maximum frame rate
