
""" Problem statement
Given a chess board of size NxN. How many possible ways are there to put N queens on it so 
that none of the put queens atack each other?
 """


# Given a chess board status and a row that the queen will be placed to
# return if that position would be possible so that that new queen is not
# being attacked by other queens already put on the board
def is_completable(board, row):

    completable = True
    for i in range(0, row):
        if(board[i] == board[row] or board[row] >= len(board) or abs(board[i] - board[row]) == abs(i - row) ):
            completable = False
            break

    return completable

#We will store all the solutions (boards) in this array
solutions = []

#Backtraking algorithm.
"""
- board is an array of size N where ith element of it is the column of the board
  and the content board[ith] is the row of the queen.
    In other words, the board [0,1,2,3] has four queens placed in (0,1), (1,1), (2,2), (3,3) 
    respectively.
- size is the length of the board
- q is the row where the candidate queen will be placed to if that placement is valid. 
    Its value by default is 0
"""
def Queens(board, size, q = 0):
    board[q] = -1
    while(board[q] < size-1):

        board[q] = board[q] + 1
        if(is_completable(board, q)):

            if(q == size - 1):
                
                solutions.append(board.copy())
                print(len(solutions))
            else:
                if((q + 1) < len(board)):
                    Queens(board, size,q+1)

# Generating an array of N size. 
# Switch it up if you want to play with this parameter ;-) (be careful!)
size_chess = 0
board = [0 for i in range(0, abs(size_chess))]
Queens(board, len(board), 0)

# Printing the total of solutions
print(len(solutions))
