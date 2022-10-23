import pygame
from threading import Timer
from win32api import GetSystemMetrics
import random
import time

#Wdith and Height
widthS = GetSystemMetrics(0)
heightS = GetSystemMetrics(1)

#x and y green
x = 400
y = 1000
#x and y red
x1 = 600
y1 = 1000
#x and y blue
x2 = 800
y2 = 1000
#x and y orange
x3 = 1000
y3 = 1000
#x and y yellow
x4 = 1200
y4 = 1000
#x and y purple
x5 = 1400
y5 = 1000

#Velocity for player
vel = 20

#Points
points = 45
point = 0

#Detects position of mouse click
cx, cy = (0, 0)

timeEachcycle = 0.0000000001

greenColor = 150, 200, 20
redColor = 250, 0, 0
blueColor = 67, 84, 255
orangeColor = 255, 165, 0
yellowColor = 255, 255, 0
purpleColor = 172, 79, 198

ifSpace = False

who_won = None

pygame.init()
def game():
    global timeEachcycle
    global x
    global y
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global x5
    global y5
    global greenColor
    global redColor
    global blueColor
    global orangeColor
    global yellowColor
    global purpleColor
    global ifSpace
    global who_won
    def cycle():
        global timeEachcycle
        global x
        global y
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        global x4
        global y4
        global x5
        global y5
        global who_won
        #if y or y1 or y2 or y3 or y4 or y5 == 800:
        time.sleep(1)
        y -= random.randint(2, 100)
        y1 -= random.randint(2, 100)
        y2 -= random.randint(2, 100)
        y3 -= random.randint(2, 100)
        y4 -= random.randint(2, 100)
        y5 -= random.randint(2, 100)
        if y < 0:
            print("green won")
            who_won = 'Green'
            timeEachcycle = 10000
        if y1 < 0:
            print("red won")
            who_won = 'Red'
            timeEachcycle = 10000
        if y2 < 0:
            print("blue won")
            who_won = 'Blue'
            timeEachcycle = 10000
        if y3 < 0:
            print("orange won")
            who_won = 'Orange'
            timeEachcycle = 10000
        if y4 < 0:
            print("yellow won")
            who_won = 'Yellow'
            timeEachcycle = 10000
        if y5 < 0:
            print("purple won")
            who_won = 'Purple'
            timeEachcycle = 10000
        Timer(timeEachcycle, cycle).start()

    win = pygame.display.set_mode((widthS, heightS))
    pygame.display.set_caption("Jumping Game 2")

    run = True

        #Keeps the window running
    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #Detects where the player clicks
            if event.type == pygame.MOUSEBUTTONUP:
                cx, cy = pygame.mouse.get_pos()
                print(cx, cy)

        keys = pygame.key.get_pressed()
            #Extras
        if keys[pygame.K_1]:
            pygame.quit()
            exit()
            #Shoot
        if keys[pygame.K_SPACE]:
            if ifSpace == False:
                ifSpace = True
                cycle()

        #Generates Font
        font = pygame.font.SysFont("comicsans", 30)
        fontBig = pygame.font.SysFont("comicsans", 150)
        fontSmall = pygame.font.SysFont("comicsans", 26)
        # Fills the screen with black
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (greenColor), (x, y, 20, 20))
        pygame.draw.rect(win, (redColor), (x1, y1, 20, 20))
        pygame.draw.rect(win, (blueColor), (x2, y2, 20, 20))
        pygame.draw.rect(win, (orangeColor), (x3, y3, 20, 20))
        pygame.draw.rect(win, (yellowColor), (x4, y4, 20, 20))
        pygame.draw.rect(win, (purpleColor), (x5, y5, 20, 20))

        pygame.draw.rect(win, (greenColor), (x + 8, y, 5, 2500))
        pygame.draw.rect(win, (redColor), (x1 + 8, y1, 5, 2500))
        pygame.draw.rect(win, (blueColor), (x2 + 8, y2, 5, 2500))
        pygame.draw.rect(win, (orangeColor), (x3 + 8, y3, 5, 2500))
        pygame.draw.rect(win, (yellowColor), (x4 + 8, y4, 5, 2500))
        pygame.draw.rect(win, (purpleColor), (x5 + 8, y5, 5, 2500))
        if who_won != None:
            whoWon = fontBig.render(f"{who_won} won!", bool(1), (255, 255, 255))
            win.blit(whoWon, (widthS / 2 - 325, heightS / 2))
        pygame.display.update()


    pygame.quit()

game()