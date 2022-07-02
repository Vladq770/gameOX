import pygame
import bot.bot_scripts as bt
import numpy as np

WIDTH = 600
HEIGHT = 600
FPS = 30
color = (255, 0, 0)
color_light = (170, 170, 170)
color_dark = (120, 120, 120)
pygame.init()
pygame.mixer.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME 10X10")
clock = pygame.time.Clock()
bg = pygame.image.load("game\\table.jpg")
gameDisplay.blit(bg, (0, 0))
pygame.display.update()
font_menu = pygame.font.SysFont('Corbel', 50)
font_end_game = pygame.font.SysFont('Corbel', 70)
text_exit = font_menu.render('EXIT', True, color)
text_play = font_menu.render('PLAY', True, color)
text_choose_x = font_menu.render('Chosse X', True, color)
text_choose_0 = font_menu.render('Chosse O', True, color)
text_x = font_menu.render('X', True, (0, 0, 0))
text_0 = font_menu.render('O', True, (0, 0, 0))
text_lose = font_end_game.render('YOU LOSE', True, (0, 0, 255))
text_win = font_end_game.render('YOU WON', True, (0, 0, 255))
text_draw = font_end_game.render('DRAW', True, (0, 0, 255))
table = np.zeros((10, 10))
running = True
menu_type = 1
isFirst = True
while running:
    clock.tick(FPS)
    mouse = pygame.mouse.get_pos()
    if menu_type == 1:
        if WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 + 20 <= mouse[1] <= HEIGHT / 2 + 80:
            pygame.draw.rect(gameDisplay, color_light, [WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 60])

        else:
            pygame.draw.rect(gameDisplay, color_dark, [WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 60])

        gameDisplay.blit(text_exit, (WIDTH / 2 - 40, HEIGHT / 2 + 28))
        if WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 - 80 <= mouse[1] <= HEIGHT / 2 - 20:
            pygame.draw.rect(gameDisplay, color_light, [WIDTH / 2 - 100, HEIGHT / 2 - 80, 200, 60])

        else:
            pygame.draw.rect(gameDisplay, color_dark, [WIDTH / 2 - 100, HEIGHT / 2 - 80, 200, 60])

        gameDisplay.blit(text_play, (WIDTH / 2 - 45, HEIGHT / 2 - 72))
    if menu_type == 2:
        if WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 + 20 <= mouse[1] <= HEIGHT / 2 + 80:
            pygame.draw.rect(gameDisplay, color_light, [WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 60])

        else:
            pygame.draw.rect(gameDisplay, color_dark, [WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 60])

        gameDisplay.blit(text_choose_x, (WIDTH / 2 - 95, HEIGHT / 2 + 28))
        if WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 - 80 <= mouse[1] <= HEIGHT / 2 - 20:
            pygame.draw.rect(gameDisplay, color_light, [WIDTH / 2 - 100, HEIGHT / 2 - 80, 200, 60])

        else:
            pygame.draw.rect(gameDisplay, color_dark, [WIDTH / 2 - 100, HEIGHT / 2 - 80, 200, 60])

        gameDisplay.blit(text_choose_0, (WIDTH / 2 - 95, HEIGHT / 2 - 72))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and menu_type > 0:
            if WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 + 20 <= mouse[1] <= HEIGHT / 2 + 80 and menu_type == 1:
                running = False
            elif WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 - 80 <= mouse[1] <= HEIGHT / 2 - 20 and menu_type == 1:
                menu_type = 2
                gameDisplay.fill((0, 0, 0))
                pygame.display.flip()
                gameDisplay.blit(bg, (0, 0))
            elif WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 + 20 <= mouse[1] <= HEIGHT / 2 + 80 and menu_type == 2:
                isFirst = True
                menu_type = 0
                gameDisplay.fill((0, 0, 0))
                pygame.display.flip()
                gameDisplay.blit(bg, (0, 0))
                continue
            elif WIDTH / 2 - 100 <= mouse[0] <= WIDTH / 2 + 100 and HEIGHT / 2 - 80 <= mouse[1] <= HEIGHT / 2 - 20 and menu_type == 2:
                isFirst = False
                menu_type = 0
                gameDisplay.fill((0, 0, 0))
                pygame.display.flip()
                gameDisplay.blit(bg, (0, 0))
                move = bt.choice_of_move(table)
                gameDisplay.blit(text_x, (move[1] * 60 + 20, move[0] * 60 + 10))
                table[move[0]][move[1]] = -1
                continue
        if event.type == pygame.MOUSEBUTTONDOWN and menu_type == 0:
            for i in range(10):
                for j in range(10):
                    if j * 60 <= mouse[0] <= j * 60 + 60 and i * 60 <= mouse[1] <= i * 60 + 60 and table[i][j] == 0:
                        if isFirst:
                            table[i][j] = 1
                            gameDisplay.blit(text_x, (j * 60 + 20, i * 60 + 10))
                            res = bt.check(table, 1)
                            if res == 1:
                                gameDisplay.blit(text_lose, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                            elif res == 2:
                                gameDisplay.blit(text_draw, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                            move = bt.choice_of_move(table)
                            gameDisplay.blit(text_0, (move[1] * 60 + 15, move[0] * 60 + 10))
                            table[move[0]][move[1]] = -1
                            res = bt.check(table, -1)
                            if res == 1:
                                gameDisplay.blit(text_win, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                            elif res == 2:
                                gameDisplay.blit(text_draw, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                        else:
                            table[i][j] = 1
                            gameDisplay.blit(text_0, (j * 60 + 15, i * 60 + 10))
                            res = bt.check(table, 1)
                            if res == 1:
                                gameDisplay.blit(text_lose, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                            elif res == 2:
                                gameDisplay.blit(text_draw, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                            move = bt.choice_of_move(table)
                            gameDisplay.blit(text_x, (move[1] * 60 + 20, move[0] * 60 + 10))
                            table[move[0]][move[1]] = -1
                            res = bt.check(table, -1)
                            if res == 1:
                                gameDisplay.blit(text_win, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
                            elif res == 2:
                                gameDisplay.blit(text_draw, (150, 100))
                                menu_type = 1
                                table[::] = 0
                                break
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()


