
test= [[1,2,3,4,5,6],
       [10,9,8,7,6,5],
       [7,6,5,4,3,2]]

## k*k max pooling with stride of 1

import numpy as np
def max_pool(mat, k_x, k_y):
    import numpy as np
    arr= np.array(mat)
    higth, width= arr.shape
    ##special case:
    if higth<k_y:
        return max_pool(mat, k_x, higth)
    if width<k_x:
        return max_pool(mat, width, k_y)
    out=[]
    for row in range(k_y-1, len(arr)):
        row_out= []
        for col in range(k_x-1, len(arr[0])):
            row_out.append(np.max(arr[row-k_y+1:row+1, col-k_x+1: col+1]))
        out.append(row_out)
    return out

test2=np.arange(6).reshape(1,6)
print(test2)
print(max_pool(test2, 2, 2))
