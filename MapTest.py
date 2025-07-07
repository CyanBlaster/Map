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
    return random.randint(1, 4)
    
def Color(x):
    if(x == 1):
        return (255, 0, 0)
    elif(x == 2):
       return (0, 255, 0)
    elif(x == 3):
       return (0, 0, 255)
    elif(x == 4):
       return (255, 0, 255)
    elif(x == 0):
        return (0, 0, 0)
    return (255, 255, 255)

def check5inARow(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[y][x] == map[y][x + 1] == map[y][x + 2] == map[y][x + 3] == map[y][x + 4] and map[y][x] >= 1 and map[y][x] <= 4):
                return True
    print(1)
    return False

def check5inACol(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[y][x] == map[y + 1][x] == map[y + 2][x] == map[y + 3][x] == map[y + 4][x] and map[y][x] >= 1 and map[y][x] <= 4):
                print(x, y)
                return True 
    print(2)    
    return False

def check5inADia1(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[y][x] == map[y + 1][x + 1] == map[y + 2][x + 2] == map[y + 3][x + 3] == map[y + 4][x + 4] and map[y][x] >= 1 and map[y][x] <= 4):
                print(x, y)
                return True
    print(3)    
    return False

def check5inADia2(map, cellAmount):
    for y in range (cellAmount - 5):
        for x in range(cellAmount - 5):
            if(map[y][x + 4] == map[y + 1][x + 3] == map[y + 2][x + 2] == map[y + 3][x + 1] == map[y + 4][x] and map[y][x] >= 1 and map[y][x] <= 4):
                print(x, y)
                return True     
    print(4)
    return False

def checkBlanks(map, cellAmount, mask):
    for y in range(cellAmount - 1, 0, -1):
        for x in range(0, cellAmount):
            if((mask[y][x] == 1 or map[y][x] == 0)):
                map[y][x] = map[y - 1][x]
                map[y - 1][x] = 0
                mask[y][x] = 0



def main():
    width = 800
    height = 800
    xIdx = 0
    yIdx = 0
    cellAmount = 20
    wCell = width/cellAmount
    hCell = height/cellAmount
    savedX = 0
    savedY = 0
    selected = False
    screen = pygame.display.set_mode((width, height))
    running = True
    map = ZeroField(cellAmount)
    mask = ZeroField(cellAmount)
    # for y in range (cellAmount):
    #     for x in range(cellAmount):
    #         map[y][x] = randomInteger()
    map[0][0] = 1
    map[1][0] = 1
    map[2][0] = 2
    map[2][1] = 1
    map[3][0] = 1
    map[4][0] = 1
    map[5][1] = 3
    map[6][1] = 3
    for i in range(cellAmount):
        checkBlanks(map, cellAmount, mask)
    while running:
            pygame.display.flip()

            if(selected):
                pygame.draw.rect(screen, (100, 100, 100), (savedX * wCell - 1, savedY * hCell - 1, 40, 40))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (savedX * wCell - 1, savedY * hCell - 1, 40, 40))

            for y in range (cellAmount):
                for x in range(cellAmount):
                    if map[y][x] != 0:
                        #print(x, y, map[y][x])
                        pygame.draw.circle(screen, Color(map[y][x]), (x * wCell + 19, y * hCell + 19), 19)
                    # if(map[y][x] == 0):
                    #     pygame.draw.rect(screen, (0, 0, 0), (x * cellAmount, y * cellAmount, 38, 38))
                    # if(map[y][x] != 0):
                        # print(x, y, map[y][x])
                
            pygame.draw.rect(screen, (255, 255, 255), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)

            




            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                        xIdx -= 1
                    elif events.key == pygame.K_RIGHT:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                        xIdx += 1
                    elif events.key == pygame.K_UP:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                        yIdx -= 1
                    elif events.key == pygame.K_DOWN:
                        pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                        yIdx += 1
                    elif events.key == pygame.K_SPACE:
                        if(selected == False):
                            selected = True
                            savedX = xIdx
                            savedY = yIdx
                            print(savedX, savedY)
                            
                        else:
                            if(abs(savedX - xIdx) <= 1 and abs(savedY - yIdx) <= 1):   
                                if((xIdx == savedX and yIdx == savedY)):
                                    selected = False
                                
                                
                                a = map[savedY][savedX]
                                map[savedY][savedX] = map[yIdx][xIdx]
                                map[yIdx][xIdx] = a
                                print(map[yIdx][xIdx])
                                selected = False

                                # if(check5inARow(map, cellAmount) == False and check5inACol(map, cellAmount) == False and check5inADia1(map, cellAmount) == False and check5inADia2(map, cellAmount) == False):
                                #     a = map[savedX][savedY]
                                #     map[savedX][savedY] = map[xIdx][yIdx]
                                #     map[xIdx][yIdx] = a

                                for y in range (cellAmount - 5):
                                    for x in range(cellAmount - 5):
                                        if(map[y][x] == map[y + 1][x] == map[y + 2][x] == map[y + 3][x] == map[y + 4][x] and map[y][x] >= 1 and map[y][x] <= 4):
                                            mask[y][x] = 1
                                            mask[y + 1][x] = 1
                                            mask[y + 2][x] = 1
                                            mask[y + 3][x] = 1
                                            mask[y + 4][x] = 1
                                            print("")
                                            selected = False

                                        if(map[y][x] == map[y + 1][x + 1] == map[y + 2][x + 2] == map[y + 3][x + 3] == map[y + 4][x + 4] and map[y][x] >= 1 and map[y][x] <= 4):
                                            print(1)
                                            mask[y][x] = 1
                                            mask[y + 1][x + 1] = 1
                                            mask[y + 2][x + 2] = 1
                                            mask[y + 3][x + 3] = 1
                                            mask[y + 4][x + 4] = 1
                                            selected = False
                                           


                                        if(map[y][x + 4] == map[y + 1][x + 3] == map[y + 2][x + 2] == map[y + 3][x + 1] == map[y + 4][x] and map[y][x] >= 1 and map[y][x] <= 4):
                                            print(2)
                                            mask[y][x + 4] = 1
                                            mask[y + 1][x + 3] = 1
                                            mask[y + 2][x + 2] = 1
                                            mask[y + 3][x + 1] = 1
                                            mask[y + 4][x] = 1
                                            selected = False
                                           
                                        if(map[y][x] == map[y][x + 1] == map[y][x + 2] == map[y][x + 3] == map[y][x + 4] and map[y][x] >= 1 and map[y][x] <= 4):
                                            mask[y][x] = 1
                                            mask[y][x + 1] = 1
                                            mask[y][x + 2] = 1
                                            mask[y][x + 3] = 1
                                            mask[y][x + 4] = 1
                                          
                                            selected = False

                                for i in range(cellAmount):
                                    checkBlanks(map, cellAmount, mask)


                                        
                                
main()