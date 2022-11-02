'''Design n-Queens matrix having first Queen placed. Use backtracking to place
remaining Queens to generate the final n-queen‘s matrix.
CODE:
'''
'''
# Python3 program to solve N Queen
# Problem using backtracking
global N
N = 4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def isSafe(board, row, col): # attacking queens
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True
# Consider this column and try placing
# this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
        # Place this queen in board[i][col]
            board[i][col] = 1
    # recur to place rest of the queens
        if solveNQUtil(board, col + 1) == True:
            return True
        # If placing queen in board[i][col
        # doesn't lead to a solution, then
        # queen from board[i][col]
        board[i][col] = 0
    # if the queen can not be placed in any row in
    # this column col then return false
    return False

def solveNQ():
    board = [ [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0] ]
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
    printSolution(board)
    return True

# Driver Code
solveNQ()
'''

#Number of queens
print ("Enter the number of queens: ")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

N_queen(N)
for i in board:
    print (i)