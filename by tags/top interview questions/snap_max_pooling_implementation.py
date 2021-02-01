
test1= [[1,2,3,4,5,6],
       [10,9,8,7,6,5],
       [7,6,5,4,3,2]]


test2= [[1,2,3],
       [10,9,8],
       [7,6,5]]

## brute force with no package:

def max_pool(mat, k_x, k_y, stride=1):
    ##first compress horizontally
    out1=[]
    for row in range(0, len(mat)):
        c_row=[]
        if len(mat[row])<k_x:
            c_row.append(max(mat[row]))
        else:
            for col in range(0, len(mat[row])-k_x+1, stride):
                c_row.append(max(mat[row][col:col+k_x]))
        out1.append(c_row)
    print(out1)

    out2=[]
    for col in range(0, len(out1[0])):
        c_col=[]
        if len(out1)<k_y:
            c_col.append(max([l[col] for l in out1]))
        else:
            for row in range(0, len(out1)-k_y+1, stride):
                #c_col.append(max(out1[row:row+k_y][col]))
                c_col.append(max([l[col] for i, l in enumerate(out1) if i>=row and i<row+k_y]))
        out2.append(c_col)
    #print(out2)
    
    return [[row[k] for row in out2] for k in range(len(out2[0]))]


    #return list(map(list, zip(*out2)))


max_pool(test1, 2, 2, stride=2)
max_pool(test2, 2, 2)




## k*k max pooling with stride of 1

import numpy as np
def max_pool(mat, k_x, k_y, stride=1):
    import numpy as np
    arr= np.array(mat)
    higth, width= arr.shape
    ##special case:
    if higth<k_y:
        return max_pool(mat, k_x, higth, stride)
    if width<k_x:
        return max_pool(mat, width, k_y, stride)
    out=[]
    for row in range(k_y-1, len(arr), stride):
        row_out= []
        for col in range(k_x-1, len(arr[0]), stride):
            row_out.append(np.max(arr[row-k_y+1:row+1, col-k_x+1: col+1]))
        out.append(row_out)
    return out

test2=np.arange(6).reshape(1,6)
print(test2)
print(max_pool(test2, 2, 2, stride=2))



##keras:
import numpy as np
from keras.models import Sequential 
from keras.layers import MaxPooling2D 
 
arr = np.array([[2, 3, 4, 2], 
                  [8, 5, 5, 1], 
                  [6, 7, 9, 4], 
                  [3, 1, 4, 5]]) 
 
#reshaping
arr = arr.reshape(1, 4, 4, 1) 
   
#define a max pooling layer
max_pool = MaxPooling2D(pool_size = 2, strides = 2)
 
#define a sequential model with just one pooling layer
model = Sequential( 
    [max_pool]) 
   
#get the output 
output = model.predict(arr) 
   
#print the output  
output = np.squeeze(output) 
print(output)

output.tolist()

def max_pooling(mat, k_x, k_y):
    import numpy as np
    from keras.models import Sequential 
    from keras.layers import MaxPooling2D
    np_mat= np.array(mat)
    x, y=np_mat.shape
    np_mat=np_mat.reshape(1, x, y, 1)
    if x<=k_x: move_x= x
    else: move_x=k_x
    if y<=k_y: move_y= y
    else: move_y=k_y
    model= Sequential([MaxPooling2D(pool_size = (move_x, move_y), strides = 1)])
    output = model.predict(np_mat)
    output= np.squeeze(output)
    return output.tolist()

test2=np.arange(6).reshape(1,6)
print(test2)

np.array(test2).shape
print(max_pooling(test2, 2, 2))