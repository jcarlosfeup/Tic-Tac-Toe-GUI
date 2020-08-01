'''
Created on 16/06/2020

TIC TAC TOE game

@author: jcarl
'''

import pygame
import GUI.Screen as GUI

def createBoard():
    board = [ ['-' for x in range(3)] for y in range(3)]
    return board


def displayBoard(board):
    for y in range(3):
        for x in range(3):
            print('|' + board[y][x] + '|',end='')
        if x == 2: print('\n')


def cellOccupied(board,x,y):
    if board[y-1][x-1] != '-':
        return True
    else:
        return False


def playMove(board,x,y,symbol):
    
    board[y-1][x-1] = symbol
    
    return board


def validPosition(pos):
    if pos != '' and pos in [1,2,3]:
        return True
    else:
        return False
    

def winGame(board):
    
    listPlaceholderX = ['X','X','X']
    listPlaceholderO = ['O','O','O']
    
    ''' check horizontal '''
    if board[0] == listPlaceholderX or board[1] == listPlaceholderX or board[2] == listPlaceholderX or board[0] == listPlaceholderO or board[1] == listPlaceholderO or board[2] == listPlaceholderO:
        return True
    
    ''' check vertical '''
    if (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        return True
    
    if (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        return True
    
    ''' check diagonal '''
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return True
    
    if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return True

    return False


if __name__ == '__main__':
        
    boardGame = createBoard()
    
    print("Welcome to the TIC TAC TOE game in Python!")

    countPlays = 1

    endGame = False
    isDigit = False
    validPos = False
    
    display = GUI.renderGUIBoard()
    
    while(not endGame):

        print("\n")
        displayBoard(boardGame)
        
        # GUI
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                endGame = True
            GUI.drawBoard(display)
            
            if event.type==pygame.MOUSEBUTTONUP:
                posSymbol = GUI.detSymbolPosO(GUI.cellClicked())
                print(posSymbol)
                GUI.drawSymbolO(display,posSymbol)
            
            pygame.display.update()

        playAgain = True
        
        ''' caso o numero seja par e a vez do player2 '''
        if countPlays%2 == 0:
            player = 'O'
            print("\nIt's Player 2 turn with symbol " + player)
        else:
            player = 'X'
            print("\nIt's Player 1 turn with symbol " + player)
        
        validPos = False
        isDigit = False
        while(playAgain or (not validPos) or (not isDigit)):
                
            posX = input("\nPlease choose position X from 1,2,3: ")
            posY = input("Please choose position Y from 1,2,3: ")
            
            if posX.isdigit() and posY.isdigit():
                posX = int(posX)
                posY = int(posY)
                isDigit = True
            else:
                print("\nPlease insert a digit for each of the positions.")
            
            if isDigit:
                if validPosition(posX) and validPosition(posY):
                    validPos = True
                else:
                    print("\nYou choose an invalid position! Please choose another one.")

            if validPos:
                if (not cellOccupied(boardGame,posX,posY)):
                    boardGame = playMove(boardGame,posX,posY,player)
                    playAgain = False
                else:
                    print("This cell is already occupied, please choose another one.")

        countPlays += 1

        if winGame(boardGame): endGame = True

    displayBoard(boardGame)
    print("\nGame finished with " + str(countPlays) + " plays made!")

