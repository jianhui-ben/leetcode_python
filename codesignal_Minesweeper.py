# Minesweeper
#In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

#Example

#For

#matrix = [[true, false, false],
#          [false, true, false],
#          [false, false, false]]
#the output should be

#minesweeper(matrix) = [[1, 2, 1],
#                       [2, 1, 1],
#                       [1, 1, 1]]
def minesweeper(matrix):
    
    out  = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    def get_val(r, c, matrix):
        if r <0 or r>=len(matrix) or c<0 or c>=len(matrix[0]):
            return 0
        return matrix[r][c]
        
    
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            out[row][col] = get_val(row-1, col-1, matrix)+get_val(row-1, col, matrix)+get_val(row-1, col+1, matrix)\
                        +get_val(row, col-1, matrix)+get_val(row, col+1, matrix)\
                        +get_val(row+1, col-1, matrix)+get_val(row+1, col, matrix)+get_val(row+1, col+1, matrix)\
            
    return out
    
    
    ##more clean approach:
    def minesweeper(matrix):

        r = []
        
        for i in range(len(matrix)):
            r.append([])
            for j in range(len(matrix[0])):
                l = -matrix[i][j]
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                            l += matrix[i+x][j+y]

                r[i].append(l)
        return r
               