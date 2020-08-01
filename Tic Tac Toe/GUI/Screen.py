'''
Created on 30/07/2020

@author: jcarl
'''

import pygame
from openpyxl.styles.colors import BLACK
from pip._vendor.html5lib._ihatexml import letter

boardWidth=600
boardHeight=600
boardHeightMargin=700

cellWidth = int(boardWidth/3)
cellHeight = int(boardHeight/3)

blackColor=(0,0,0)
blueColor=(0,0,255)
redColor=(255,0,0)


def drawBoard(display):
    
    #vertical lines
    pygame.draw.rect(display,blackColor,[200,0,20,boardHeight],0)
    pygame.draw.rect(display,blackColor,[400,0,20,boardHeight],0)
    
    #horizontal lines
    pygame.draw.rect(display,blackColor,[0,200,boardWidth,20],0)
    pygame.draw.rect(display,blackColor,[0,400,boardWidth,20],0)


def drawSymbolO(display,pos):    

    radius = 80
    symbolWidth = 5
    
    pygame.draw.circle(display,redColor, pos, radius,symbolWidth)
    
    
def drawSymbolX(display):

    symbolWidth=5
    
    pygame.draw.line(display, blueColor,(0,0),(200,200),symbolWidth)
    pygame.draw.line(display, blueColor,(0,200),(200,0),symbolWidth)


#returns an integer (1-6) representing the area of the cell that was clicked
#1  2  3
#4  5  6
#7  8  9
def cellClicked():
    
    posx,posy = pygame.mouse.get_pos()
    
    if posx >= 0 and posx <= cellWidth and posy >= 0 and posy <= cellHeight:
        return 1
    elif posx >= cellWidth and posx <= (cellWidth*2) and posy >= 0 and posy <= cellHeight:
        return 2
    elif posx >= (cellWidth*2) and posx <= boardWidth and posy >= 0 and posy <= cellHeight:
        return 3
    elif posx >= 0 and posx <= cellWidth and posy >= cellHeight and posy <= (cellHeight*2):
        return 4
    elif posx >= cellWidth and posx <= (cellWidth*2) and posy >= cellHeight and posy <= (cellHeight*2):
        return 5
    elif posx >= (cellWidth*2) and posx <= boardWidth and posy >= cellHeight and posy <= (cellHeight*2):
        return 6
    elif posx >= 0 and posx <= cellWidth and posy >= (cellHeight*2) and posy <= boardHeight:
        return 7
    elif posx >= cellWidth and posx <= (cellWidth*2) and posy >= (cellHeight*2) and posy <= boardHeight:
        return 8
    elif posx >= (cellWidth*2) and posx <= boardWidth and posy >= (cellHeight*2) and posy <= boardHeight:
        return 9
    else:
        0
        
def detSymbolPosO(cellNumber):
    
    posX = int(boardWidth/6)
    posY = int(boardHeight/6)
    margin = 10
    
    if cellNumber==1:
        return (posX,posY)
    elif cellNumber==2:
        return ( cellWidth+posX++margin,posY)
    elif cellNumber==3:
        return ( (margin+cellWidth*2)+posX,posY)
    elif cellNumber==4:
        return (posX,cellHeight+posY+margin)
    elif cellNumber==5:
        return (cellWidth+posX+margin,cellHeight+posY+margin)
    elif cellNumber==6:
        return ( (margin+cellWidth*2)+posX,cellHeight+posY+margin)
    elif cellNumber==7:
        return (posX,(cellHeight*2)+posY+margin)
    elif cellNumber==8:
        return (cellWidth+posX+margin,(cellHeight*2)+posY+margin)
    elif cellNumber==9:
        return ( (cellWidth*2)+posX+margin,(cellHeight*2)+posY+margin)
    

#font_style = pygame.font.SysFont("bahnschrift", 25)

def renderTurn(display,score_font,player_no):
    
    if player_no==1:
        letterColor = blueColor
    else:
        letterColor = redColor
        
    value = score_font.render("Player " + str(player_no) + " turn", True,letterColor)
    display.blit(value, [0,boardHeight])

def renderGUIBoard():
    pygame.init()
    
    display = pygame.display.set_mode(size=(boardWidth, boardHeightMargin))
    display.fill([255,255,255])
    
    pygame.display.set_caption('Tic Tac Toe')
    score_font = pygame.font.SysFont("arial", 35)
    renderTurn(display,score_font,2)
    drawBoard(display)
    pygame.display.update()
    
    return display
    

if __name__ == '__main__':
    
    pygame.init()
    display = pygame.display.set_mode(size=(boardWidth, boardHeightMargin))
    display.fill([255,255,255])
    
    pygame.display.set_caption('Tic Tac Toe')
    pygame.display.update()

    score_font = pygame.font.SysFont("arial", 35)
    renderTurn(display,score_font,2)
    drawBoard(display)

    endGame = False
    while not endGame:
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                endGame = True
            
            if event.type==pygame.MOUSEBUTTONUP:
                posSymbol = detSymbolPosO(cellClicked())
                print(posSymbol)
                drawSymbolO(display,posSymbol)
            
            pygame.display.update()
   
    pygame.quit()
    quit()
   
                                     
