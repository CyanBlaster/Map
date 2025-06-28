import sys
import pygame
import datetime
import math
import pygame.freetype
import random

pygame.init()


def ZeroField(n):
    return [[0] * n for i in range(n)]

def randomInteger():
    return random.randint(1, 5)
    
def Color(x):
    if(x == 1):
         return (255, 0, 0)
    elif(x == 2):
       return (0, 255, 0)
    elif(x == 3):
       return (0, 0, 255)
    elif(x == 4):
       return (255, 0, 255)
    return (0, 0, 0)
def main():
    width = 800
    height = 800
    xIdx = 0
    yIdx = 0
    cellAmount = 40
    savedX = 0
    savedY = 0
    selected = False
    screen = pygame.display.set_mode((width, height))
    running = True
    map = ZeroField(cellAmount)
    for y in range (cellAmount):
        for x in range(cellAmount):
            a = randomInteger()
            map[x][y] = a
            pygame.draw.circle(screen, Color(map[x][y]), (x * cellAmount + 19, y * cellAmount + 19), 19)

    while running:
            for y in range (cellAmount):
                for x in range(cellAmount):
                  pygame.draw.circle(screen, Color(map[x][y]), (x * cellAmount + 19, y * cellAmount + 19), 19)



            pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 40, 40), 1, border_radius = 1)
            pygame.display.flip()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 40, 40), 1, border_radius = 1)
                        xIdx -= 1
                    elif events.key == pygame.K_RIGHT:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 40, 40), 1, border_radius = 1)
                        xIdx += 1
                    elif events.key == pygame.K_UP:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 40, 40), 1, border_radius = 1)
                        yIdx -= 1
                    elif events.key == pygame.K_DOWN:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 40, 40), 1, border_radius = 1)
                        yIdx += 1
                    elif events.key == pygame.K_SPACE:
                        if(selected == False):
                            selected = True
                            savedX = xIdx
                            savedY = yIdx
                        else:
                            if(abs(savedX - xIdx) <= 1 and abs(savedY - yIdx) <= 1):
                                selected = False
                                a = map[savedX][savedY]
                                map[savedX][savedY] = map[xIdx][yIdx]
                                map[xIdx][yIdx] = a
                        
main()