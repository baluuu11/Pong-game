import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
grey = (128, 128, 128)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")

rocket1X = 10
rocket1Y = 250
rocket1SizeX = 20
rocket1SizeY = 130
rocket1Move = 0
Rocket1Mode = 0

rocket2X = 770
rocket2Y = 250
rocket2SizeX = 20
rocket2SizeY = 130
rocket2Move = 0
Rocket2Mode = 0

ballX = 400
ballY = 300
ballR = 10
ballSpeed = 10
ballmoveX = ballSpeed
ballmoveY = -ballSpeed

fps = pygame.time.Clock()


def Text(text, color, pos):
    text = str(text)
    font = pygame.font.SysFont('Andale Mono, monospace', 40)
    textWrite = font.render(text, False, color)
    screen.blit(textWrite, pos)


menu = True
run = True
while run:

    while menu:
        score1 = 0
        score2 = 0
        Rocket1Mode = 0
        Rocket2Mode = 0
        rocket1SizeY = 130
        rocket2SizeY = 130
        ballR = 10
        ballSpeed = 10
        ballX = 400
        ballY = 300
        ballmoveY = 5
        ballmoveX = 5
        rocket2X = 770
        rocket2Y = 250
        rocket1X = 10
        rocket1Y = 250
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ballSpeed = 10
                    Rocket2Mode = -2
                    menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    ballSpeed = 12
                    Rocket2Mode = 5
                    menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    ballSpeed = 15
                    Rocket2Mode = 10
                    menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    ballSpeed = 20
                    Rocket2Mode = 15
                    Rocket1Mode = 15
                    menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                    ballSpeed = random.choice(range(11, 30))
                    Rocket2Mode = random.choice(range(15, 35))
                    Rocket1Mode = random.choice(range(15, 35))
                    rocket1SizeY = random.choice(range(100, 200))
                    rocket2SizeY = random.choice(range(100, 200))
                    ballR = random.choice(range(5, 30))
                    menu = False
        Text("[1] Easy ", white, (200, 150))
        Text("[2] Medium ", white, (200, 200))
        Text("[3] Hard ", white, (200, 250))
        Text("[4] Speed mode ", white, (200, 300))
        Text("[5] Random mode ", white, (200, 350))
        Text("Move keys w/s  m-menu  Esc-exit", grey, (20, 550))
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rocket1Move = -10 - Rocket1Mode
            if event.key == pygame.K_s:
                rocket1Move = +10 + Rocket1Mode
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rocket1Move = 0
            if event.key == pygame.K_s:
                rocket1Move = 0

    if rocket1Y <= 0:
        rocket1Y = 0
    if rocket1Y >= 470:
        rocket1Y = 470
    if rocket2Y <= 0:
        rocket2Y = 0
    if rocket2Y >= 470:
        rocket2Y = 470

    if ballY <= 0:
        ballmoveY = +ballSpeed
    if ballY >= 600:
        ballmoveY = -ballSpeed
    if ballX <= 0:
        ballmoveX = +ballSpeed
        score2 += 1
    if ballX >= 800:
        ballmoveX = -ballSpeed
        score1 += 1

    if ballX <= rocket1X + rocket1SizeX:
        if ballX + ballR >= rocket1X:
            if ballY >= rocket1Y:
                if ballY + ballR <= rocket1Y + rocket1SizeY:
                    ballmoveX = +ballSpeed

    if ballX <= rocket2X + rocket2SizeX:
        if ballX + ballR >= rocket2X:
            if ballY >= rocket2Y:
                if ballY + ballR <= rocket2Y + rocket2SizeY:
                    ballmoveX = -ballSpeed

    if rocket2Y < ballY:
        rocket2Move = 15 + Rocket2Mode
    if rocket2Y > ballY:
        rocket2Move = -15 - Rocket2Mode

    rocket1Y += rocket1Move
    rocket2Y += rocket2Move
    ballX += ballmoveX
    ballY += ballmoveY

    screen.fill(black)
    pygame.draw.rect(screen, white, [rocket1X, rocket1Y, rocket1SizeX, rocket1SizeY])
    pygame.draw.rect(screen, white, [rocket2X, rocket2Y, rocket2SizeX, rocket2SizeY])
    pygame.draw.line(screen, white, [400, 0], [400, 800], 3)
    pygame.draw.line(screen, white, [320, 0], [320, 80], 3)
    pygame.draw.line(screen, white, [480, 0], [480, 80], 3)
    pygame.draw.line(screen, white, [320, 80], [480, 80], 3)
    pygame.draw.circle(screen, white, [ballX, ballY], ballR)

    scoreFont = pygame.font.SysFont('times new roman', 50)
    score1Text = str(score1)
    Score1Render = scoreFont.render(score1Text, True, white)
    screen.blit(Score1Render, (350, 10))

    score2Text = str(score2)
    Score2Render = scoreFont.render(score2Text, True, white)
    screen.blit(Score2Render, (430, 10))

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_m:
            screen.fill(black)
            menu = True
    if score1 >= 3:
        screen.fill(black)
        Text("You Win, Congratulation!!", blue, (100, 50))
        menu = True
    if score2 >= 3:
        screen.fill(black)
        Text("Computer Win, Try one more time.", blue, (20, 50))
        menu = True

    pygame.display.flip()
    fps.tick(60)

pygame.quit()
quit()
