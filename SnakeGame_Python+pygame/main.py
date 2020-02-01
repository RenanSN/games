import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((500, 500)) # Tamanho da tela
pygame.display.set_caption('Snake')

#Cobra
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((52,73,94)) # Cor da cobra

#Maçã
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((105,47,45)) # cor da maçã

#direção que inicia
my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(5) # Velocidade
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    #colisão com a maçã
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    # movimentação da cabeça e sobre posição da cobra
    for i in range(len(snake) -1 , 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Movimentação
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((39,174,96)) # Cor de fundo
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()