import pygame
import random

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('final_sound.wav')

width = 400
height = 450
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('2048 GAME')
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font(None, 24)
fullscreen = False

# colors
color_0 = (255, 255, 255)
color_2 = (230, 250, 255)
color_4 = (179, 240, 255)
color_8 = (128, 229, 255)
color_16 = (77, 219, 255)
color_32 = (0, 204, 255)
color_64 = (0, 163, 204)
color_128 = (179, 255, 236)
color_256 = (102, 255, 217)
color_512 = (0, 230, 172)
color_1024 = (0, 153, 115)
color_2048 = (217, 179, 255)
color_light_text = (235, 235, 224)
color_dark_text = (16, 16, 10)
black = (0, 0, 0)
white = (255, 255, 255)
color_background = (230, 204, 179)
color_higher = (115, 75, 38)
colors = {0: color_0,
          2: color_2,
          4: color_4,
          8: color_8,
          16: color_16,
          32: color_32,
          64: color_64,
          128: color_128,
          256: color_256,
          512: color_512,
          1024: color_1024,
          2048: color_2048,
          '> 2048': color_higher,
          'light_text': color_light_text,
          'dark_text': color_dark_text,
          'black': black,
          'white': white,
          'background': color_background}

background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (width, height))


values = [[0 for _ in range(4)] for _ in range(4)]
game_is_done = False
new_appearance = True
tiles_at_the_start = 0
swipe = ''
score = 0


def end_draw():
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 30)
    restart_text = font.render('Press Enter to Restart', True, colors['dark_text'])
    final_score_text = font.render(f'This is your score: {score}', True, colors['dark_text'])
    font = pygame.font.Font(None, 35)
    end_text = font.render('You have finished the game!', True, colors['dark_text'])
    screen.blit(end_text, (45, 160))
    screen.blit(final_score_text, (95, 230))
    screen.blit(restart_text, (95, 300))


def swipe_tiles(swipe, board):
    global score
    tiles_already_merged = [[False for _ in range(4)] for _ in range(4)]
    if swipe == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for k in range(i):
                        if board[k][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not tiles_already_merged[i - shift][j] and not tiles_already_merged[i - shift - 1][j]:
                        board[i - shift - 1][j] = 2 * board[i - shift - 1][j]
                        board[i - shift][j] = 0
                        tiles_already_merged[i - shift - 1][j] = True
                        score += board[i - shift - 1][j]
    elif swipe == 'DOWN':
        for i in range(3):
            for j in range(4):
                shift = 0
                for k in range(i + 1):
                    if board[3 - k][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not tiles_already_merged[3 - i + shift][j] and not tiles_already_merged[2 - i + shift][j]:
                        board[3 - i + shift][j] = 2 * board[3 - i + shift][j]
                        board[2 - i + shift][j] = 0
                        tiles_already_merged[3 - i + shift][j] = True
                        score += board[3 - i + shift][j]
    elif swipe == 'LEFT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for k in range(j):
                    if board[i][k] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j - shift] == board[i][j - shift - 1] and not tiles_already_merged[i][j - shift - 1] and not tiles_already_merged[i][j - shift]:
                    board[i][j - shift - 1] = 2 * board[i][j - shift - 1]
                    board[i][j - shift] = 0
                    tiles_already_merged[i][j - shift - 1] = True
                    score += board[i][j - shift - 1]
    elif swipe == 'RIGHT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for k in range(j):
                    if board[i][3 - k] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not tiles_already_merged[i][4 - j + shift] and not tiles_already_merged[i][3 - j + shift]:
                        board[i][4 - j + shift] = 2 * board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        tiles_already_merged[i][4 - j + shift] = True
                        score += board[i][4 - j + shift]

    return board


def new_random_tiles(board):
    board_is_full = True
    count = 0
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if board[row][col] == 0:
            count += 1
            board_is_full = False
            board[row][col] = 2
    if count < 1:
        board_is_full = True
    return board, board_is_full


def board():
    score_text = font.render(f'Score: {score}', True, colors['dark_text'])
    screen.blit(score_text, (10, 410))
    pass


def tiles(board):
    for i in range(len(board)):
        for j in range(len(board)):
            value = board[i][j]
            if value == 64 or value == 1024:
                value_color = colors['light_text']
            else:
                value_color = colors['dark_text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['> 2048']
            pygame.draw.rect(screen, color, [j * 98 + 10, i * 98 + 10, 85, 85], 0, 0)
            if value > 0:
                value_length = len(str(value))
                font = pygame.font.Font(None, 56 - (4 * value_length))
                text_in_tiles = font.render(str(value), True, value_color)
                text_centering = text_in_tiles.get_rect(center = (j * 98 + 53, i * 98 + 53))
                screen.blit(text_in_tiles, text_centering)
                pygame.draw.rect(screen, colors['black'], [j * 98 + 10, i * 98 + 10, 85, 85], 2, 0)


def display_instructions():
    screen.blit(background_image, (0, 0))
    instruction_text = [
        "                        How to Play:",
        "Use arrow keys (UP/DOWN/LEFT/RIGHT)",
        "              or 'WASD' to move tiles.",
        "     Merge tiles with the same number",
        "                 to get higher values.",
        "              Press 'ENTER' to start.",
        "       Press 'F' to toggle fullscreen."
    ]
    y_offset = 100
    for line in instruction_text:
        text = font.render(line, True, colors['dark_text'])
        screen.blit(text, (50, y_offset))
        y_offset += 30
    pygame.display.flip()


display_instructions()

running = False

while not running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            running = True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


pygame.mixer.music.play(-1)


while running:
    clock.tick(fps)
    screen.blit(background_image, (0, 0))

    board()
    tiles(values)
    if new_appearance or tiles_at_the_start < 2:
        values, game_is_done = new_random_tiles(values)
        new_appearance = False
        tiles_at_the_start += 1
    if swipe != '':
        values = swipe_tiles(swipe, values)
        swipe = ''
        new_appearance = True
    if game_is_done:
        end_draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                swipe = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                swipe = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                swipe = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                swipe = 'RIGHT'

            if game_is_done:
                if event.key == pygame.K_RETURN:
                    values = [[0 for _ in range(4)] for _ in range(4)]
                    new_appearance = True
                    tiles_at_the_start = 0
                    score = 0
                    swipe = ''
                    game_is_done = False

            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    background_image = pygame.transform.scale(background_image, (800, 500))
                    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((width, height))
                    background_image = pygame.transform.scale(background_image, (width, height))

    pygame.display.flip()

pygame.quit()