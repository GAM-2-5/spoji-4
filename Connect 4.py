import numpy as np
import pygame
import sys

def create_board():
    board = np.zeros((n_row,n_col))
    return board

def printb(board):
    print(np.flip(board, 0))

def valid_location(board, col):
     return board[n_row - 1][col]== 0
    
def next_row(board, col):
    for row in range (n_row):
        if board[row][col]== 0:
            return row
        
def drop(board, row, col, piece):
    board[row][col] = piece

def win(board, piece):
    #provjeri horizontalne kombinacije
    for c in range (n_col - 3):
        for r in range (n_row):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #provjeri vertikalne kombinacije
    for c in range (n_col):
        for r in range (n_row - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

def drawb(board,x):
    pygame.draw.rect(screen, blue , [0, x, width, heightb])
    pomy= x//2
    pomx= x//2
    for row in range (n_row):
        ž=n_row-row
        for col in range (n_col):
            if board[row][col]==0:
                pygame.draw.circle(screen, blank, [pomx + col*x, pomy + ž*x], r)
            if board[row][col]==1:
                pygame.draw.circle(screen, player1boja, [pomx + col*x, pomy+ ž*x], r)
            if board[row][col]==2:
                pygame.draw.circle(screen, player2boja, [pomx + col*x, pomy + ž*x], r)
                
def col1(leadx):
    return int(leadx // sqr_size)
    
def postavke():
    n_row= int(input('Izaberite broj redova vaše ploče:(max 20)'))
    
pink = (255, 200, 200)
purple = (177, 156, 217)
white = (255, 255, 255)
blue = (170,175,255)
#zadane postavke
n_row = 6
n_col = n_row + 1
width = 700
height = width
sqr_size = int(width/n_col)
heightb = width - sqr_size
r = sqr_size//2 - 2
player1boja = pink
player2boja = purple
blank = white

board = create_board()
gam_over = False
turn = 0

##mjenjaj= input('Želite li promjeniti zadane postavke igre spoji 4? (DA/NE)')
##if mjenjaj == 'DA':
##    postavke()

pygame.init()  
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('THE SPOJI 4 GAME')

leadx = sqr_size//2
leady = sqr_size//2

while not gam_over:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if leadx == sqr_size//2: pass
                else: leadx -= sqr_size
            if event.key == pygame.K_RIGHT:
                leadx += sqr_size
                if leadx > width: leadx -= sqr_size
            if event.key == pygame.K_DOWN:
                #Player1 input
                if turn == 0:
                    boja = player1boja
                    col = col1(leadx)
                    if valid_location(board, col):
                            row = next_row(board, col)
                            drop(board, row, col, 1)
                    if win(board, 1):
                            print ('Player1 je pobjedio!')
                            gam_over = True 
                #Player2 input
                if turn == 1:
                    boja = player2boja
                    col = col1(leadx)
                    if valid_location(board, col):
                            row = next_row(board, col)
                            drop(board, row, col, 2)
                    if win(board, 2):
                            print ('Player2 je pobjedio!')
                            gam_over = True 
                            
            turn+= 1
            turn = turn % 2
                            
        screen.fill(blank)
        pygame.draw.circle(screen, pink, [leadx, leady], r)
        drawb(board, sqr_size)
        pygame.display.update()
            
pygame.quit()
