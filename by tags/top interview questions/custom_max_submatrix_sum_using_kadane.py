## max sub array sum and give index of start and end
def kadane(l):
    if not l: return None
    max_sum, cur_max=0, 0
    start, end, temp= None, None, 0
    for i in range(len(l)):
        cur_max+=l[i]
        if cur_max>max_sum:
            max_sum= cur_max
            start= temp
            end= i+1
        if cur_max<0:
            cur_max=0
            temp=i+1
    return max_sum, start, end

test=[-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(test))


## max submatrix sum:
def max_matrix(mat):
    if not mat: return None
    row, column= len(mat), len(mat[0])
    max_sum, final_right, final_left, final_top, final_down=float("-inf"), 0, 0, 0, 0
    for left in range(column):
        for right in range(left, column):
            temp=[None] * row
            for i in range(row):
                temp[i]= sum(mat[i][left: right+1])
            cur_sum, top, down= kadane(temp)
            if cur_sum> max_sum:
                max_sum=cur_sum
                final_right, final_left, final_top, final_down=\
                    right+1, left, top, down
    return max_sum, final_right, final_left, final_top, final_down
                    
M = [[1, 2, -1, -4, -20],
 [-8, -3, 4, 2, 1],
 [3, 8, 10, 1, 3],
 [-4, -1, 1, 7, -6]]
 
# Function call
print(max_matrix(M))         
    
