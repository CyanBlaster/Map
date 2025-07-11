import sys
import pygame
import datetime
import math
import pygame.freetype
import random

pygame.init()

GAME_FONT = pygame.freetype.Font("DayDream.ttf", 24)

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

def NumRepeatedInColumn(map, startX, startY):
    i = 1
    while(startY + i <= len(map) - 1 and map[startY][startX] == map[startY + i][startX] and map[startY + i][startX] != 0):
        i += 1
    return i


def ColumnDisappear(map, startX, startY, mask, m):
    a = NumRepeatedInColumn(map, startX, startY)
    if(a >= m):
        for i in range(a):
            mask[startY + i][startX] = 1
        return True
    return False
        
def NumRepeatedInRow(map, startX, startY):
    i = 1
    while(startX + i <= len(map) - 1 and map[startY][startX] == map[startY][startX + i] and map[startY][startX + i] != 0):
        i += 1
    return i
def RowDisappear(map, startX, startY, mask, m):
    a = NumRepeatedInRow(map, startX, startY)
    if(a >= m):
        for i in range(a):
            mask[startY][startX + i] = 1
        return True
    return False
       

def NumRepeatedInDia1(map, startX, startY):
    i = 1
    while(startX + i <= len(map) - 1 and startY + i <= len(map) - 1 and map[startY][startX] == map[startY + i][startX + i] and map[startY + i][startX + i] != 0):
        i += 1
    return i

def Dia1Disappear(map, startX, startY, mask, m):
    a = NumRepeatedInDia1(map, startX, startY)
    if(a >= m):
        for i in range(a):
            mask[startY + i][startX + i] = 1
        return True
    return False
        

def NumRepeatedInDia2(map, startX, startY):
    i = 1
    while(startX - i >= 0  and startY + i <= len(map) - 1 and map[startY][startX] == map[startY + i][startX - i] and map[startY + i][startX - i] != 0):
        i += 1
    return i

def Dia2Disappear(map, startX, startY, mask, m):
    a = NumRepeatedInDia2(map, startX, startY)
    if(a >= m):
        for i in range(a):
            mask[startY + i][startX - i] = 1
        return True
    return False
        
    



def checkBlanks(map, cellAmount, mask):
    add = 0
    for y in range(0, cellAmount):
        for x in range(0, cellAmount):
            if((mask[y][x] == 1 or map[y][x] == 0)):
                if(mask[y][x] == 1):
                    add += 1
                map[y][x] = map[y - 1][x]
                map[y - 1][x] = 0
                mask[y][x] = 0
    return add




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
    minimumLen = 5
    score = 0
    screen = pygame.display.set_mode((width + 200, height))
    running = True
    map = ZeroField(cellAmount)
    mask = ZeroField(cellAmount)
    for y in range (cellAmount):
        for x in range(cellAmount):
            map[y][x] = randomInteger()
    # map = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [4, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    for i in range(cellAmount):
        checkBlanks(map, cellAmount, mask)
    while running:
            pygame.display.flip()
            screen.fill((0, 0, 0))

            text_surface, rect = GAME_FONT.render("Score:", (255, 0, 0))
            text, rect = GAME_FONT.render(str(score), (255, 0, 0))
            screen.blit(text_surface, (850, 300))
            screen.blit(text, (850, 340))

            if(selected):
                pygame.draw.rect(screen, (100, 100, 100), (savedX * wCell - 1, savedY * hCell - 1, 40, 40))
            else:
                pygame.draw.rect(screen, (1, 1, 1), (savedX * wCell - 1, savedY * hCell - 1, 40, 40))
                

            for y in range (cellAmount):
                for x in range(cellAmount):
                        #print(x, y, map[y][x])
                        if(map[y][x] == 0):
                            map[y][x] = randomInteger()
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
                        if(xIdx > 0):
                            pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                            xIdx -= 1
                    elif events.key == pygame.K_RIGHT:
                        if(xIdx < cellAmount - 1):
                            pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                            xIdx += 1
                    elif events.key == pygame.K_UP:
                        if(yIdx > 0):
                            pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                            yIdx -= 1
                    
                    elif events.key == pygame.K_DOWN:
                        if(yIdx < cellAmount - 1):
                            pygame.draw.rect(screen, (0, 0, 0), (xIdx * wCell - 1, yIdx * hCell - 1, 40, 40), 1, border_radius = 1)
                            yIdx += 1


                    elif events.key == pygame.K_1:
                        print(NumRepeatedInColumn(map, xIdx, yIdx))
                        

                    elif events.key == pygame.K_SPACE:
                        if(selected == False):
                            selected = True
                            savedX = xIdx
                            savedY = yIdx
                        
                            
                        else:
                            if(abs(savedX - xIdx) <= 1 and abs(savedY - yIdx) <= 1):   
                                if((xIdx == savedX and yIdx == savedY)):
                                    selected = False
                                
                                a = map[savedY][savedX]
                                map[savedY][savedX] = map[yIdx][xIdx]
                                map[yIdx][xIdx] = a
                                # print(map[yIdx][xIdx])
                                selected = False
                                
                                c = True
                                r = True
                                d = True
                                D = True



                                while(c and r and d and D):
                                    for y in range (cellAmount - 1):
                                        for x in range(cellAmount):
                                            c = ColumnDisappear(map, x, y, mask, minimumLen)
                                    for y in range (cellAmount):
                                        for x in range(cellAmount - 1):
                                            r = RowDisappear(map, x, y, mask, minimumLen)
                                    for y in range (cellAmount - 1):
                                        for x in range(cellAmount - 1):
                                            d = Dia1Disappear(map, x, y, mask, minimumLen)
                                    for y in range (cellAmount - 1, 0, -1):
                                        for x in range(cellAmount - 1, 0, -1):
                                            D = Dia2Disappear(map, x, y, mask, minimumLen)
                                    for i in range(cellAmount):
                                        score += checkBlanks(map, cellAmount, mask)

main()