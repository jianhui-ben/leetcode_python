#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321

## my solution: O(log n) time / O(1) space

def reverse(x: int):
    pos= x>=0
    number= [i for i in str(abs(x))]
    if len(number)<=1:
        return x
    for i in range(len(number)//2):
        number[len(number)-1-i], number[i]=number[i], number[len(number)-1-i]
    out=int(''.join(number)) if pos else -int(''.join(number))
    return out if out in range(-2**31, 2**31-1) else 0
      
reverse(122424230)

## similar solution proposed in leetcode:
## it create two variables
def reverse(x: int):
    res = 0
    while x!=0:
        res = res*10 + x%10;
        x = x//10
    return res if res in range(-2**31, 2**31-1) else 0

