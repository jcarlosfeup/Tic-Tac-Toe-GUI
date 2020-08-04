'''
Created on 30/07/2020

@author: jcarl
'''

import pygame

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
    

def drawSymbolX(display,cellNumber):

    margin = 20
    symbolWidth=5
    
    if cellNumber==1:
        pygame.draw.line(display, blueColor,(margin,margin),(cellWidth-margin,cellHeight-margin),symbolWidth)
        pygame.draw.line(display, blueColor,(margin,cellHeight-margin),(cellWidth-margin,margin),symbolWidth)
    elif cellNumber==2:
        pygame.draw.line(display, blueColor,(cellWidth+(margin*2),margin),( (cellWidth*2)-margin,cellHeight-margin),symbolWidth)
        pygame.draw.line(display, blueColor,(cellWidth+(margin*2),cellHeight-margin),( (cellWidth*2)-margin,margin),symbolWidth)
    elif cellNumber==3:
        pygame.draw.line(display, blueColor,((cellWidth*2)+(margin*2),margin),((cellWidth*3)-margin,cellHeight-margin),symbolWidth)
        pygame.draw.line(display, blueColor,((cellWidth*2)+(margin*2),cellHeight-margin),( (cellWidth*3)-margin,margin),symbolWidth)
    elif cellNumber==4:
        pygame.draw.line(display, blueColor,(margin,cellHeight+(margin*2)),(cellWidth-margin,(cellHeight*2)-margin),symbolWidth)
        pygame.draw.line(display, blueColor,(margin,(cellHeight*2)-margin),(cellWidth-margin,cellHeight+(margin*2)),symbolWidth)
    elif cellNumber==5:
        pygame.draw.line(display, blueColor,(cellWidth+(margin*2),cellHeight+(margin*2)),((cellWidth*2)-margin,(cellHeight*2)-margin),symbolWidth)
        pygame.draw.line(display, blueColor,(cellWidth+(margin*2),(cellHeight*2)-margin),((cellWidth*2)-margin,cellHeight+(margin*2)),symbolWidth)
    elif cellNumber==6:
        pygame.draw.line(display, blueColor,((cellWidth*2)+(margin*2),cellHeight+(margin*2)),((cellWidth*3)-margin,(cellHeight*2)-margin),symbolWidth)
        pygame.draw.line(display, blueColor,((cellWidth*2)+(margin*2),(cellHeight*2)-margin),((cellWidth*3)-margin,cellHeight+(margin*2)),symbolWidth)
    elif cellNumber==7:
        pygame.draw.line(display, blueColor,(margin,(cellHeight*2)+(margin*2)),(cellWidth-margin,(cellHeight*3)-margin),symbolWidth)
        pygame.draw.line(display, blueColor,(margin,(cellHeight*3)-margin),(cellWidth-margin,(cellHeight*2)+(margin*2)),symbolWidth)
    elif cellNumber==8:
        pygame.draw.line(display, blueColor,(cellWidth+(margin*2),(cellHeight*2)+(margin*2)),((cellWidth*2)-margin,(cellHeight*3)-margin),symbolWidth)
        pygame.draw.line(display, blueColor,(cellWidth+(margin*2),(cellHeight*3)-margin),((cellWidth*2)-margin,(cellHeight*2)+(margin*2)),symbolWidth)
    elif cellNumber==9:
        pygame.draw.line(display, blueColor,((cellWidth*2)+(margin*2),(cellHeight*2)+(margin*2)),((cellWidth*3)-margin,(cellHeight*3)-margin),symbolWidth)
        pygame.draw.line(display, blueColor,((cellWidth*2)+(margin*2),(cellHeight*3)-margin),((cellWidth*3)-margin,(cellHeight*2)+(margin*2)),symbolWidth)
    
    
def drawSymbolO(display,pos):
    radius = 80
    symbolWidth = 5
    pygame.draw.circle(display,redColor,pos,radius,symbolWidth)


def renderTurn(display,player):
    
    if player=='X':
        letterColor = blueColor
        player_no = 1
    else:
        letterColor = redColor
        player_no = 2
    
    score_font = pygame.font.SysFont("arial", 35)
    #clears area if something is there first
    display.fill(pygame.Color("white"), (boardWidth/3, boardHeight, 200, 40))
    value = score_font.render("Player " + str(player_no) + " turn", True,letterColor)
    display.blit(value, [boardWidth/3,boardHeight])
    
def clearTurn(display):
    
    display.fill(pygame.Color("black"), (0, boardHeight, 110, 40))
    
    

def renderGUIBoard():
    pygame.init()
    
    display = pygame.display.set_mode(size=(boardWidth, boardHeightMargin))
    display.fill([255,255,255])
    
    pygame.display.set_caption('Tic Tac Toe')
    drawBoard(display)
    
    pygame.display.update()
    
    return display
    

if __name__ == '__main__':
    
    pygame.init()
    display = pygame.display.set_mode(size=(boardWidth, boardHeightMargin))
    display.fill([255,255,255])
    
    pygame.display.set_caption('Tic Tac Toe')

    renderTurn(display,2)
    drawBoard(display)
    
    pygame.display.update()

    endGame = False
    while not endGame:
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                endGame = True
            
            if event.type==pygame.MOUSEBUTTONUP:
                posSymbol = detSymbolPosO(cellClicked())
                print(posSymbol)
                #drawSymbol(display,posSymbol,'X')
            
            pygame.display.update()
   
    pygame.quit()
    quit()
   
                                     
