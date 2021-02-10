#289. Game of Life
#According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

#The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#Any live cell with fewer than two live neighbors dies as if caused by under-population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by over-population.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
         ## better method: denote live --> die as -1 and die --> live as 2
        """
        Do not return anything, modify board in-place instead.
        """
        high, wid= len(board), len(board[0])
        def move(row, col, s):
            if row<0 or col<0 or row>=high or col>=wid:
                return s
            else:
                if type(board[row][col])==int:
                    return s+board[row][col]
                else:
                    return s+board[row][col][0]
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                s= 0
                s=move(row-1,col,s)
                s=move(row-1,col-1,s)
                s=move(row-1,col+1,s)                 
                s=move(row,col-1, s)
                s=move(row,col+1, s)
                s=move(row+1,col, s)
                s=move(row+1,col-1, s)
                s=move(row+1,col+1, s)
                    
                if ((type(board[row][col])==int and board[row][col]==0) or \
                    (type(board[row][col])!=int and board[row][col][0]==0)) and s!=3:
                    board[row][col]=(0, 0)
                elif ((type(board[row][col])==int and board[row][col]==0) or \
                    (type(board[row][col])!=int and board[row][col][0]==0)) and s==3:
                    board[row][col]=(0, 1)
                elif ((type(board[row][col])==int and board[row][col]==1) or \
                    (type(board[row][col])!=int and board[row][col][0]==1)) and (s<2 or s>3):
                    board[row][col]=(1, 2)
                else:
                    board[row][col]=(1, 3)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col][1]==0 or board[row][col][1]==2:
                    board[row][col]=0
                else:
                    board[row][col]=1
                    
                
                
# P(next head | 10 heads before) = P(next head ^ 10 heads before) / P(10 heads before)
#= [P( next head ^ 10 heads before ^ it's a fair coin) +  P( next head ^ 10 heads before ^ it's a error coin) ] / [ P(10 heads before ^ it's a fair coin)  + P(10 heads before ^ its a error coin) ]
#= [ P(11 heads ^ its a fair coin) +  P(11 heads ^ its a error coin) ] /  [ P(10 heads before ^ it's a fair coin)  + P(10 heads before ^ its a error coin) ]
#= [ 0.5**11 * 999/1000 + 1.0**11 * 1/1000] + [ 0.5**10 * 999/1000 + 1.0**10 * 1/1000 ]
#=0.753089                   


#P(next head | 10 heads before)=

# P(next head ^ 10 heads before)/ P(10 heads before)
# (P(next head ^ 10 heads before ^ it's fair coin ) + P(next head ^ 10 heads before ^ it's unfair))
# / (P(10 heads before ^ fair) + P(10 heads before ^ unfair))
# = (P(11 heads ^ fair) + P(11 heads ^ unfair) )
# / (P(10 heads ^ fair) + P(10 heads ^ unfair) )
#= ((0.5**11* 999/1000)+ (1/1000))
# / ((0.5**10* 999/1000)+ (1/1000))
print(((0.5**11* 999/1000)+ (1/1000))/ ((0.5**10* 999/1000)+ (1/1000)))


#100个post 0.04概率出广告， back to back ads个数的期望
