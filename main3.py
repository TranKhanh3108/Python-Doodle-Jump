import random

import pygame

pygame.init()

#libraly of game contants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128,128,128)
width = 400
height = 650
background = white
player = pygame.transform.scale(pygame.image.load('nhanvat.png'), (70, 70))
fps = 60
font = pygame.font.Font('UTM AvoBold.ttf',16)
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False

#game variables
player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
score_last = 0
super_jump = 2
jump_last = 0

#create screen
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption(('Doodle Jump'))

#check for collisison with blocks
def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and jump == False and y_change > 0:
            j = True
    return j

#update player y position every loop
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = 0.4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos

#handle movenment of platfroms as game progresses
# xử lý sự di chuyển của các nền đất khi trò chơi tiến triển
def update_platforms(my_list, y_pos, change):
    global score
    if y_pos < 350 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    for item in range(len(my_list)):
        if my_list[item][1] > 600:
            my_list[item] = [random.randint(10, 420), random.randint(-50, -10), 70, 10]
            score += 1
    return my_list  # sửa lại câu lệnh return


running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))
    blocks = []
    score_text = font.render('High score: ' + str(high_score), True, black, background)
    screen.blit(score_text, (380, 10))
    high_score_text = font.render('Score: ' + str(score), True, black, background)
    screen.blit(high_score_text, (420, 30))

    score_text = font.render('Air Jump (Spacebar) ' + str(super_jump), True, black, background)
    screen.blit(score_text, (20, 20))
    if game_over:
        game_over_text = font.render('Game over: Spacebar to restart! ', True, black, background)
        screen.blit(game_over_text, (120, 80))


    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, black, platforms[i])
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                player_x = 170
                player_y = 400
                background = white
                score_last = 0
                super_jump = 2
                jump_last = 0
                platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
            if event.key == pygame.K_SPACE and not game_over and super_jump > 0:
                super_jump -= 1
                y_change = -15
            if event.key == pygame.K_LEFT:
                x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0

    jump = check_collisions(blocks, jump)
    player_x += x_change

    if player_y < 600:
        player_y = update_player(player_y)
    else:
        game_over = True
        y_change = 0
        x_change = 0

    platforms = update_platforms(platforms, player_y, y_change)

    if player_x < -20:
        player_x = -20
    elif player_x > 330:
        player_x = 330

    if x_change > 0:
        player = pygame.transform.scale(pygame.image.load('nhanvat.png'), (70, 70))
    elif x_change < 0:
        player = pygame.transform.flip(pygame.transform.scale(pygame.image.load('nhanvat.png'), (70, 70)), 1, 0)

    if score > high_score:
        high_score = score

    if score - score_last > 15:
        score_last = score
        background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    if score - jump_last > 50:
        jump_last = score
        super_jump += 1

    pygame.display.flip()
pygame.quit()