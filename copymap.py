import sys
import pygame
import datetime
import math
import pygame.freetype
import random

pygame.init()


def ZeroField(n):
    return [[0] * n for i in range(n)]
def ZeroTuple(n):
    return [[(0, 0, 0)] * n for i in range(n)]

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

def checkBlanks(map2, cellAmount):
    for y in range(cellAmount - 1, 0, -1):
        for x in range(cellAmount):
            if(map2[x][y] == (0, 0, 0) and y != 0):
                map2[x][y] = map2[x][y -1]
                map2[x][y - 1] = (0, 0, 0)



def main():
    width = 800
    height = 800
    xIdx = 0
    yIdx = 0
    cellAmount = 5
    screen = pygame.display.set_mode((width, height))
    running = True
    map = ZeroField(cellAmount)
    map2 = ZeroTuple(cellAmount)

    for y in range(cellAmount):
        for x in range(cellAmount):
            map2[x][y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    while running:

            screen.fill((0, 0, 0))
            

            for y in range(cellAmount):
                for x in range(cellAmount):
                    if (map[x][y] == 1):
                        pygame.draw.rect(screen, (255, 255, 255), (x * 160 + 1, y * 160 + 1, 158, 158))
                    pygame.draw.circle(screen, map2[x][y], (x * height/cellAmount + height/cellAmount/ 2 + 1, y * width/cellAmount + width/cellAmount/ 2 + 1), 78)
            
            pygame.draw.rect(screen, (255, 255, 0), (xIdx * 160 + 1, yIdx * 160 + 1, 158, 158), 1, border_radius = 1)

            pygame.display.flip()

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 160, 160), 1, border_radius = 1)
                        if(xIdx > 0):
                            xIdx -= 1
                    elif events.key == pygame.K_RIGHT:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 160, 160), 1, border_radius = 1)
                        if(xIdx < cellAmount - 1):
                            xIdx += 1
                    elif events.key == pygame.K_UP:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 160, 160), 1, border_radius = 1)
                        if(yIdx > 0):
                            yIdx -= 1
                    elif events.key == pygame.K_DOWN:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 160, 160), 1, border_radius = 1)
                        if(yIdx < cellAmount - 1):
                            yIdx += 1
                    elif events.key == pygame.K_SPACE: 
                        if(map[xIdx][yIdx] == 0):
                            map[xIdx][yIdx] = 1
                        elif(map[xIdx][yIdx] == 1):
                            map[xIdx][yIdx] = 0
                    elif events.key == pygame.K_RETURN:
                        for y in range(cellAmount):
                            for x in range(cellAmount):
                                if (map[x][y] == 1):
                                    map2[x][y] = (0, 0, 0)
                                    map[x][y] = 0


                        for i in range(0, cellAmount - 1):
                            checkBlanks(map2, cellAmount)

                                    

            
                           
main()