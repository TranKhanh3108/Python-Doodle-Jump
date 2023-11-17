import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128,128, 128)
WIDTH = 400
HEIGHT = 500
background = white
player = pygame.transform.scale(pygame.image.load('nhanvat.png'),(50,50))
fps = 60
font = pygame.font.Font('UTM AvoBold.ttf',16)
timer = pygame.time.Clock()

#Thực thể
player_x=170
player_y=400
platform=[[175, 480, 60, 5]]
jump = False

#Tao cua so
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Doodle Jumper")

#Update vi tri truc y cua nhan vat
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = 1

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)

    blocks = []

    for i in range(len(platform)):
        block =pygame.draw.rect(screen, black, platform[i], 0, 3)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player_y = update_player(player_y)

    pygame.display.flip()
pygame.quit()
