import pygame
import sys
import os
import random


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 30)


def move_left():
    wizard_rect.right -= 4



def move_right():
    if wizard_rect.right >= 400:
        wizard_rect.right += 0
    else:
        wizard_rect.right += 2


def rand_level():
    num = random.randrange(250, 550, 1)
    return num


def score_display(points, h_points):
    score_string_surface = game_font.render(f'SCORE: {points}', True, (0, 0, 0))
    score_string_rect = score_string_surface.get_rect(center=(960, 950))
    score_high_surface = game_font.render(f'HIGH SCORE: {h_points}', True, (0, 0, 0))
    score_high_rect = score_high_surface.get_rect(center=(960, 1000))
    screen.blit(score_string_surface, score_string_rect)
    screen.blit(score_high_surface, score_high_rect)


def rand_monster(platforms):
    num = random.randrange(3, platforms, 1)
    return num


def monster(b, num):
    pos = b[num].centerx
    return pos


# VARIABLES
dis = 450
platform_how_many = 20
a = []
floor_position_x = 0
floor_position_y = rand_level()
wizard_movement_y = 0
gravity = 0.05
move_jump = False
go_right = False
game_active = False
platform_speed = 4
is_fire = False
bullet_fly = 60
bullet_y = 0
bullet_x = 0
game_fail = False
avatar_choose = 0
score_add = False
score_how_many = 0
score_high_score = 0
monster_pos = rand_monster(platform_how_many)
monster_a = []
monster_last = False
boss_dead = False
# Add monster pos to monster_a
monster_a.append(monster_pos)
# Colors
SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHT_GREEN = (0, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 128)
LIGHT_BLUE = (0, 0, 255)
RED = (200, 0, 0)
LIGHT_RED = (255, 100, 100)
PURPLE = (102, 0, 102)
LIGHT_PURPLE = (153, 0, 153)
# Game init
pygame.init()
screen = pygame.display.set_mode((1920, 1200))
clock = pygame.time.Clock()
game_font = pygame.font.Font('assets/rainyhearts.ttf', 40)
# Display surface
bg_surface = pygame.image.load('assets/background1.png').convert()
# Wizard surface
wizard_surface = pygame.image.load('assets/wizard2.png')
wizard_rect = wizard_surface.get_rect(center=(100, 200))
wizard_surface1 = pygame.image.load('assets/wizard3.png')
wizard_rect1 = wizard_surface1.get_rect(center=(100, 200))
# Floor surface
floor_surface = pygame.image.load('assets/ground3.png').convert()
# generate platforms
for i in range(0, platform_how_many):
    floor_rect69 = floor_surface.get_rect(topleft=(floor_position_x, floor_position_y))
    a.append(floor_rect69)
    floor_position_x += dis
    floor_position_y = rand_level()

# Game over
game_over_surface = pygame.image.load('assets/gameover.png')
game_over_rect = game_over_surface.get_rect(center=(960, 500))
press_space_surface = pygame.image.load('assets/pressspace.png')
press_space_rect = press_space_surface.get_rect(center=(950, 700))
# Bullet
bullet_surface = pygame.image.load('assets/bullet1.png')
bullet_rect = bullet_surface.get_rect(center=(0, 0))
# Monster
monster_surface = pygame.image.load('assets/blastoise1.png')
monster_rect = monster_surface.get_rect(center=(950, 200))
# Avatar
avatar_string_surface = pygame.image.load('assets/avatar_choose.png')
avatar_string_rect = avatar_string_surface.get_rect(center=(960, 300))
# Button
button_surface = pygame.image.load('assets/button3.png')
button_rect = button_surface.get_rect(center=(0, 0))
# Score
score_surface = pygame.image.load('assets/score.png')
score_rect = score_surface.get_rect(center=(960, 300))
# Boss
boss_surface = pygame.image.load('assets/boss1.png')
# Floor dark
floor_dark_surface = pygame.image.load('assets/grounddark1.png')
floor_dark_rect = floor_dark_surface.get_rect(center=(0, 0))

# Control game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Type key
    keys = pygame.key.get_pressed()
    if game_active:
        if keys[pygame.K_LEFT]:
            move_left()
            score_add = False
        if keys[pygame.K_RIGHT]:
            move_right()
            go_right = True
            score_add = False
        else:
            go_right = False
        if keys[pygame.K_UP]:
            score_add = False
            move_jump = True
        # Shoot
        if keys[pygame.K_f]:
            score_add = False
            is_fire = True
            bullet_y = wizard_rect.centery
            bullet_x = wizard_rect.right
            bullet_fly = 50
    # RESET if space and game active False
    if keys[pygame.K_SPACE] and game_active == False and game_fail == True:
        wizard_movement_y = 0
        gravity = 0.5
        wizard_rect.centery = 100
        wizard_rect.centerx = 200
        game_active = True
        is_fire = False
        boss_dead = False
        monster_last = False
        monster_a.clear()
        monster_pos = rand_monster(platform_how_many)
        monster_a.append(monster_pos)

        n = 0
        for i in range(0, (len(a) - 0)):
            a[i].left = n
            n += dis
        if score_how_many >= score_high_score:
            score_high_score = score_how_many
        score_how_many = 0
    # EXIT
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
# THE GAME:
    # Choose Avatar
    if game_active == False and game_fail == False and boss_dead == False:
        screen.blit(bg_surface, (0, 0))
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        # 1 avatar
        if 745 + 100 > mouse[0] > 745 and 390 + 130 > mouse[1] > 390:
            # pygame.draw.rect(bg_surface, RED, (745, 390, 100, 130))
            screen.blit(button_surface, (745, 390, 100, 130))
            screen.blit(wizard_surface, (760, 400, 100, 50))
            screen.blit(wizard_surface1, (1060, 400, 100, 50))
            if click[0] == 1:
                avatar_choose = 0
                game_active = True
        # 2 avatar
        elif 1060 + 100 > mouse[0] > 1060 and 390 + 130 > mouse[1] > 390:
            # pygame.draw.rect(bg_surface, RED, (1060, 390, 100, 130))
            screen.blit(button_surface, (1060, 390, 100, 130))
            screen.blit(wizard_surface, (760, 400, 100, 50))
            screen.blit(wizard_surface1, (1060, 400, 100, 50))
            if click[0] == 1:
                avatar_choose = 1
                game_active = True

        # Both
        else:
            # pygame.draw.rect(bg_surface, GREEN, (745, 390, 100, 130))
            screen.blit(wizard_surface, (760, 400, 100, 50))
            # pygame.draw.rect(bg_surface, GREEN, (1060, 390, 100, 130))
            screen.blit(wizard_surface1, (1060, 400, 100, 50))

        screen.blit(avatar_string_surface, avatar_string_rect)
    # Game started
    if game_active:
        screen.blit(bg_surface, (0, 0))
        score_display(score_how_many, score_high_score)
        wizard_movement_y += gravity
        wizard_rect.bottom += wizard_movement_y
        if avatar_choose == 0:
            screen.blit(wizard_surface, wizard_rect)
        elif avatar_choose == 1:
            screen.blit(wizard_surface1, wizard_rect)
        if wizard_rect.top >= 1200:
            game_active = False
            game_fail = True
        # Jump
        if move_jump:
            for n in range(15):
                wizard_rect.top -= 1
            move_jump = False
        # Fire loop
        if is_fire:
            bullet_rect.centerx = bullet_x + bullet_fly
            bullet_rect.centery = bullet_y
            screen.blit(bullet_surface, bullet_rect)
            bullet_fly += 5
            if bullet_rect.centerx >= 1920:
                bullet_fly = 20
                bullet_y = wizard_rect.centery
                bullet_x = wizard_rect.right
                is_fire = False
                score_add = False
        # Move screen with wizard
        if wizard_rect.right >= 400 and go_right:
            for rect in a:
                rect.right -= platform_speed
        # Spot the monster
        if monster_rect.colliderect(bullet_rect):
            if monster_pos == platform_how_many - 1:
                print(f'\tWylosowano ostatnią platformę')
                monster_last = True
            if not monster_last:
                print("BOOM")
                print(f'\tpoprzednia pozycja {monster_pos} , tabela {monster_a} ')
                monster_pos = rand_monster(platform_how_many)
                print(f'\tzastrzeliłem potwora i wylosowałem platforme {monster_pos}')
                for i in monster_a:
                    while monster_pos <= i:
                        print(f'\twylosowana platforma {monster_pos} jest mniejsza od wartości {i} w tabeli {monster_a}')
                        print(f'\tLosuje na nowo\n')
                        monster_pos = rand_monster(platform_how_many)
                        print(f'\twylosowana nowa platforma {monster_pos}')

                    else:
                        print(f'\twylosowana platforma {monster_pos} jest większa od wartości {i} w tabeli {monster_a}')

                monster_a.append(monster_pos)
                print(f'\tnowa pozycja potwora {a[monster_pos].centerx} oraz tabela {monster_a}\n')
            score_add = True
            bullet_rect.centerx = wizard_rect.centery
            bullet_rect.centery = wizard_rect.right
            score_how_many += 1
        if score_add and monster_last == False:
            screen.blit(score_surface, score_rect)
            is_fire = False
        elif score_add == False and monster_last == False:
            monster_rect.centerx = monster(a, monster_pos) + 70
            monster_rect.centery = a[monster_pos].centery - 70
            screen.blit(monster_surface, monster_rect)
        # KILL MONSTERS
        elif score_add and monster_last:
            is_fire = False
        # Write Platform
        for floor in a:
            if wizard_rect.colliderect(floor):
                gravity = 0
                wizard_movement_y = 0
            else:
                gravity = 0.5

        for rect in a:
            screen.blit(floor_surface, rect)
        # Write Boss platform
        floor_dark_position_x = (a[(platform_how_many - 1)].centerx + 400)
        platform_dark_a = []
        for i in range(0, 3):
            floor_dark_rect = floor_dark_surface.get_rect(topleft=(floor_dark_position_x, 800))
            platform_dark_a.append(floor_dark_rect)
            floor_dark_position_x += 497
        for rect in platform_dark_a:
            screen.blit(floor_dark_surface, rect)
        # Boss platform collison
        for floor_dark in platform_dark_a:
            if wizard_rect.colliderect(floor_dark):
                gravity = 0
                wizard_movement_y = 0
            else:
                gravity = 0.5
        # Boss
        boss_x = platform_dark_a[2].centerx
        boss_y = platform_dark_a[2].top - 65
        boss_rect = boss_surface.get_rect(center=(boss_x, boss_y))
        if boss_dead == False:
            screen.blit(boss_surface, boss_rect)
        # Boss shot
        if boss_rect.colliderect(bullet_rect):
            you_win_surface = game_font.render(f'THE END', True, (0, 0, 0))
            you_win_rect = you_win_surface.get_rect(center=(960, 400))
            win_rest_surface = game_font.render(f'PRESS SPACE TO RESTAR', True, (0, 0, 0))
            win_rest_rect = win_rest_surface.get_rect(center=(960, 450))
            screen.blit(you_win_surface, you_win_rect)
            screen.blit(win_rest_surface, win_rest_rect)
            boss_dead = True
            is_fire = False
            game_active = False
            game_fail = True

    # Game Over
    if game_active == False and game_fail == True and boss_dead == False:
        screen.blit(game_over_surface, game_over_rect)
        screen.blit(press_space_surface, press_space_rect)

    pygame.display.update()
    clock.tick(120)
