'''
Created on 05/08/2020

TIC TAC TOE game

Module providing the Graphical user interface logic

@author: Carlos Portela
'''
import pygame

BOARD_WIDTH=600
BOARD_HEIGHT=600
BOARD_HEIGHT_MARGIN=700
CELL_WIDTH = int(BOARD_WIDTH/3)
CELL_HEIGHT = int(BOARD_HEIGHT/3)

BLACK_COLOR=(0,0,0)
BLUE_COLOR=(0,0,255)
RED_COLOR=(255,0,0)


def drawBoard(display):
    
    thickness = 20
    
    #vertical lines
    pygame.draw.rect(display,BLACK_COLOR,[CELL_WIDTH,0,thickness,BOARD_HEIGHT],0)
    pygame.draw.rect(display,BLACK_COLOR,[CELL_WIDTH*2,0,thickness,BOARD_HEIGHT],0)
    
    #horizontal lines
    pygame.draw.rect(display,BLACK_COLOR,[0,CELL_HEIGHT,BOARD_WIDTH,thickness],0)
    pygame.draw.rect(display,BLACK_COLOR,[0,CELL_HEIGHT*2,BOARD_WIDTH,thickness],0)


#returns an integer (1-9) representing the area of the cell that was clicked
#1  2  3
#4  5  6
#7  8  9
def cellClicked():
    
    posx,posy = pygame.mouse.get_pos()
    
    if posx >= 0 and posx <= CELL_WIDTH and posy >= 0 and posy <= CELL_HEIGHT:
        return 1
    elif posx >= CELL_WIDTH and posx <= (CELL_WIDTH*2) and posy >= 0 and posy <= CELL_HEIGHT:
        return 2
    elif posx >= (CELL_WIDTH*2) and posx <= BOARD_WIDTH and posy >= 0 and posy <= CELL_HEIGHT:
        return 3
    elif posx >= 0 and posx <= CELL_WIDTH and posy >= CELL_HEIGHT and posy <= (CELL_HEIGHT*2):
        return 4
    elif posx >= CELL_WIDTH and posx <= (CELL_WIDTH*2) and posy >= CELL_HEIGHT and posy <= (CELL_HEIGHT*2):
        return 5
    elif posx >= (CELL_WIDTH*2) and posx <= BOARD_WIDTH and posy >= CELL_HEIGHT and posy <= (CELL_HEIGHT*2):
        return 6
    elif posx >= 0 and posx <= CELL_WIDTH and posy >= (CELL_HEIGHT*2) and posy <= BOARD_HEIGHT:
        return 7
    elif posx >= CELL_WIDTH and posx <= (CELL_WIDTH*2) and posy >= (CELL_HEIGHT*2) and posy <= BOARD_HEIGHT:
        return 8
    elif posx >= (CELL_WIDTH*2) and posx <= BOARD_WIDTH and posy >= (CELL_HEIGHT*2) and posy <= BOARD_HEIGHT:
        return 9
    else:
        0
        
def detSymbolPosO(cellNumber):
    
    posX = int(BOARD_WIDTH/6)
    posY = int(BOARD_HEIGHT/6)
    margin = 10

    if cellNumber==1:
        return (posX,posY)
    elif cellNumber==2:
        return ( CELL_WIDTH+posX++margin,posY)
    elif cellNumber==3:
        return ( (margin+CELL_WIDTH*2)+posX,posY)
    elif cellNumber==4:
        return (posX,CELL_HEIGHT+posY+margin)
    elif cellNumber==5:
        return (CELL_WIDTH+posX+margin,CELL_HEIGHT+posY+margin)
    elif cellNumber==6:
        return ( (margin+CELL_WIDTH*2)+posX,CELL_HEIGHT+posY+margin)
    elif cellNumber==7:
        return (posX,(CELL_HEIGHT*2)+posY+margin)
    elif cellNumber==8:
        return (CELL_WIDTH+posX+margin,(CELL_HEIGHT*2)+posY+margin)
    elif cellNumber==9:
        return ( (CELL_WIDTH*2)+posX+margin,(CELL_HEIGHT*2)+posY+margin)
    

def drawSymbolX(display,cellNumber):

    margin = 20
    symbolWidth=5
    
    if cellNumber==1:
        pygame.draw.line(display, BLUE_COLOR,(margin,margin),(CELL_WIDTH-margin,CELL_HEIGHT-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,(margin,CELL_HEIGHT-margin),(CELL_WIDTH-margin,margin),symbolWidth)
    elif cellNumber==2:
        pygame.draw.line(display, BLUE_COLOR,(CELL_WIDTH+(margin*2),margin),( (CELL_WIDTH*2)-margin,CELL_HEIGHT-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,(CELL_WIDTH+(margin*2),CELL_HEIGHT-margin),( (CELL_WIDTH*2)-margin,margin),symbolWidth)
    elif cellNumber==3:
        pygame.draw.line(display, BLUE_COLOR,((CELL_WIDTH*2)+(margin*2),margin),((CELL_WIDTH*3)-margin,CELL_HEIGHT-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,((CELL_WIDTH*2)+(margin*2),CELL_HEIGHT-margin),( (CELL_WIDTH*3)-margin,margin),symbolWidth)
    elif cellNumber==4:
        pygame.draw.line(display, BLUE_COLOR,(margin,CELL_HEIGHT+(margin*2)),(CELL_WIDTH-margin,(CELL_HEIGHT*2)-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,(margin,(CELL_HEIGHT*2)-margin),(CELL_WIDTH-margin,CELL_HEIGHT+(margin*2)),symbolWidth)
    elif cellNumber==5:
        pygame.draw.line(display, BLUE_COLOR,(CELL_WIDTH+(margin*2),CELL_HEIGHT+(margin*2)),((CELL_WIDTH*2)-margin,(CELL_HEIGHT*2)-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,(CELL_WIDTH+(margin*2),(CELL_HEIGHT*2)-margin),((CELL_WIDTH*2)-margin,CELL_HEIGHT+(margin*2)),symbolWidth)
    elif cellNumber==6:
        pygame.draw.line(display, BLUE_COLOR,((CELL_WIDTH*2)+(margin*2),CELL_HEIGHT+(margin*2)),((CELL_WIDTH*3)-margin,(CELL_HEIGHT*2)-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,((CELL_WIDTH*2)+(margin*2),(CELL_HEIGHT*2)-margin),((CELL_WIDTH*3)-margin,CELL_HEIGHT+(margin*2)),symbolWidth)
    elif cellNumber==7:
        pygame.draw.line(display, BLUE_COLOR,(margin,(CELL_HEIGHT*2)+(margin*2)),(CELL_WIDTH-margin,(CELL_HEIGHT*3)-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,(margin,(CELL_HEIGHT*3)-margin),(CELL_WIDTH-margin,(CELL_HEIGHT*2)+(margin*2)),symbolWidth)
    elif cellNumber==8:
        pygame.draw.line(display, BLUE_COLOR,(CELL_WIDTH+(margin*2),(CELL_HEIGHT*2)+(margin*2)),((CELL_WIDTH*2)-margin,(CELL_HEIGHT*3)-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,(CELL_WIDTH+(margin*2),(CELL_HEIGHT*3)-margin),((CELL_WIDTH*2)-margin,(CELL_HEIGHT*2)+(margin*2)),symbolWidth)
    elif cellNumber==9:
        pygame.draw.line(display, BLUE_COLOR,((CELL_WIDTH*2)+(margin*2),(CELL_HEIGHT*2)+(margin*2)),((CELL_WIDTH*3)-margin,(CELL_HEIGHT*3)-margin),symbolWidth)
        pygame.draw.line(display, BLUE_COLOR,((CELL_WIDTH*2)+(margin*2),(CELL_HEIGHT*3)-margin),((CELL_WIDTH*3)-margin,(CELL_HEIGHT*2)+(margin*2)),symbolWidth)
    
    
def drawSymbolO(display,pos):
    radius = 80
    symbolWidth = 5
    pygame.draw.circle(display,RED_COLOR,pos,radius,symbolWidth)


def renderStatement(display,player,statement):
    
    padding = 10
    
    if player=='X':
        letterColor = BLUE_COLOR
        player_no = 1
    else:
        letterColor = RED_COLOR
        player_no = 2

    score_font = pygame.font.SysFont("arial", 35)
    
    #replaces the TBD by the number of the player
    statReplaced = statement.replace("TBD",str(player_no))
    
    #clears area if something is there first
    display.fill(pygame.Color("white"), ((BOARD_WIDTH/2)-(len(statReplaced)*6)-padding,BOARD_HEIGHT+padding, 300, 40))
    
    value = score_font.render(statReplaced,True,letterColor)
    display.blit(value, [ (BOARD_WIDTH/2)-(len(statReplaced)*6),BOARD_HEIGHT+padding])
    

def renderGUIBoard():
    pygame.init()

    display = pygame.display.set_mode(size=(BOARD_WIDTH, BOARD_HEIGHT_MARGIN))
    display.fill([255,255,255])
    
    pygame.display.set_caption('Tic Tac Toe')
    drawBoard(display)
    
    pygame.display.update()
    
    return display                    
