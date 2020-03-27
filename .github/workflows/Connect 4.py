import numpy as np

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

    
        

n_row = 6 #int(input('Izaberite broj redova vaše ploče:'))
n_col = 7 #int(input('Izaberite broj stupaca vaše ploče:'))

board = create_board()
printb(board)
gam_over = False
turn = 0

while not gam_over:
    #Player1 input
    if turn == 0:
        col = int(input('Player1 izaberite stupac (0-{}):'.format(n_col- 1)))

        if valid_location(board, col):
            row = next_row(board, col)
            drop(board, row, col, 1)

        if win(board, 1):
            print ('Player1 je pobjedio!')
            gam_over= True
            
    #Player2 input
    else:
        col = int(input('Player2 izaberite stupac (0-{}):'.format(n_col- 1 )))

        if valid_location(board, col):
            row = next_row(board, col)
            drop(board, row, col, 2)

        if win(board, 2):
            print ('Player2 je pobjedio!')
            gam_over= True
            
    printb(board)
            
    turn+= 1
    turn = turn % 2
