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
    elif(x == 5):
        return (0, 0, 0)
    return (255, 255, 255)

def check5inARow(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[x][y] == map[x + 1][y] == map[x + 2][y] == map[x + 3][y] == map[x + 4][y] and map[x][y] >= 1 and map[x][y] <= 4):
                return True
    print(1)
    return False

def check5inACol(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[x][y] == map[x][y + 1] == map[x][y + 2] == map[x][y + 3] == map[x][y + 4] and map[x][y] >= 1 and map[x][y] <= 4):
                print(x, y)
                return True 
    print(2)    
    return False

def check5inADia1(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[x][y] == map[x + 1][y + 1] == map[x + 2][y + 2] == map[x + 3][y + 3] == map[x + 4][y + 4] and map[x][y] >= 1 and map[x][y] <= 4):
                print(x, y)
                return True 
    print(3)    
    return False

def check5inADia2(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[x][y + 4] == map[x + 1][y + 3] == map[x + 2][y + 2] == map[x + 3][y + 1] == map[x + 4][y] and map[x][y] >= 1 and map[x][y] <= 4):
                print(x, y)
                return True     
    print(4)
    return False

def checkBlanks(map, cellAmount):
    for y in range(cellAmount - 1, 0, -1):
        for x in range(cellAmount):
            if((map[x][y] == 5 or map[x][y] == 6) and y != 0):
                map[x][y] = map[x][y - 1]
                map[x][y - 1] = 5



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
    for i in range(0, cellAmount):
        checkBlanks(map, cellAmount)
        
    while running:
            pygame.display.flip()

            if(selected):
                pygame.draw.rect(screen, (100, 100, 100), (savedX * cellAmount - 1, savedY * cellAmount - 1, 40, 40))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (savedX * cellAmount - 1, savedY * cellAmount - 1, 40, 40))

            for y in range (cellAmount):
                for x in range(cellAmount):
                  pygame.draw.circle(screen, Color(map[x][y]), (x * cellAmount + 19, y * cellAmount + 19), 19)
            pygame.draw.rect(screen, (255, 255, 255), (xIdx * cellAmount - 1, yIdx * cellAmount - 1, 40, 40), 1, border_radius = 1)




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
                                if((xIdx == savedX and yIdx == savedY)):
                                    selected = False
                                
                                a = map[savedX][savedY]
                                map[savedX][savedY] = map[xIdx][yIdx]
                                map[xIdx][yIdx] = a

                                if(check5inARow(map, cellAmount) == False and check5inACol(map, cellAmount) == False and check5inADia1(map, cellAmount) == False and check5inADia2(map, cellAmount) == False):
                                    a = map[savedX][savedY]
                                    map[savedX][savedY] = map[xIdx][yIdx]
                                    map[xIdx][yIdx] = a

                                for y in range (cellAmount - 5):
                                    for x in range(cellAmount - 5):
                                        if(map[x][y] == map[x + 1][y] == map[x + 2][y] == map[x + 3][y] == map[x + 4][y] and map[x][y] >= 1 and map[x][y] <= 4):
                                            map[x][y] = 6
                                            map[x + 1][y] = 6
                                            map[x + 2][y] = 6
                                            map[x + 3][y] = 6
                                            map[x + 4][y] = 6
                                            selected = False

                                        elif(map[x][y] == map[x + 1][y + 1] == map[x + 2][y + 2] == map[x + 3][y + 3] == map[x + 4][y + 4] and map[x][y] >= 1 and map[x][y] <= 4):
                                            print(1)
                                            map[x][y] = 6
                                            map[x + 1][y + 1] = 6
                                            map[x + 2][y + 2] = 6
                                            map[x + 3][y + 3] = 6
                                            map[x + 4][y + 4] = 6
                                            selected = False
                                           


                                        elif(map[x][y + 4] == map[x + 1][y + 3] == map[x + 2][y + 2] == map[x + 3][y + 1] == map[x + 4][y] and map[x][y] >= 1 and map[x][y] <= 4):
                                            print(2)
                                            map[x][y + 4] = 6
                                            map[x + 1][y + 3] = 6
                                            map[x + 2][y + 2] = 6
                                            map[x + 3][y + 1] = 6
                                            map[x + 4][y] = 6
                                            selected = False
                                           
                                        elif(map[x][y] == map[x][y + 1] == map[x][y + 2] == map[x][y + 3] == map[x][y + 4] and map[x][y] >= 1 and map[x][y] <= 4):
                                            map[x][y] = 6
                                            map[x][y + 1] = 6
                                            map[x][y + 2] = 6
                                            map[x][y + 3] = 6
                                            map[x][y + 4] = 6
                                          
                                            selected = False

                                for i in range(0, cellAmount):
                                    checkBlanks(map, cellAmount)


                                        
                                
main()