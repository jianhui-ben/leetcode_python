#Implement int sqrt(int x).

#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

#Since the return type is an integer, the decimal digits are truncated and 
#only the integer part of the result is returned.

#Example 1:

#Input: 4
#Output: 2

def mySqrt(x: int) -> int:
    ## binary serach in range(0: x)
    if x==1:
        return 1
    max, min= x, 1
    cur_index= int(0.5* (max+min))
    while not (cur_index**2<=x and (cur_index+1)**2>x):
        if cur_index**2>x:  ##too large
            max, min= cur_index-1, min
            cur_index=int(0.5* (max+min))
        else: 
            max, min= max, cur_index+1
            cur_index=int(0.5*(min+max))
    return cur_index

mySqrt(6)###2