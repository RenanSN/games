import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,500)
    y = random.randint(0,500)
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
my_direction = RIGHT

clock = pygame.time.Clock()

# Pontuação
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False

while not game_over:
    clock.tick(1) # Velocidade
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT

    #colisão com a maçã
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    # Verifica se a cobra colidiu com as boras
    if snake[0][0] == 500 or snake[0][1] == 500 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # Verifique se a cobra atingiu a si mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    # movimentação da cabeça e sobre posição da cobra
    #for i in range(len(snake) - 1, 0, -1):
    #    snake[i] = (snake[i-1][0], snake[i-1][1])

    snake.pop()

    # Actually make the snake move.
    if my_direction == UP:
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    if my_direction == DOWN:
        snake.insert(0, (snake[0][0], snake[0][1] + 10))
    if my_direction == RIGHT:
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))
    if my_direction == LEFT:
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))

    screen.fill((39,174,96)) # Cor de fundo
    screen.blit(apple,apple_pos)

    for x in range(0, 500, 10): # Desenhar linhas verticais
        pygame.draw.line(screen, (47, 54, 64), (x, 0), (x, 500))
    for y in range(0, 500, 10): # Desenhar linhas horizontal
        pygame.draw.line(screen, (47, 54, 64), (0, y), (500, y))
    
    score_font = font.render('Score: %s' % (score), True, (0,0,0))
    score_rect = score_font.get_rect()
    score_rect.topleft = (500 - 120, 15)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (232, 65, 24))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (500 / 2, 170)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()