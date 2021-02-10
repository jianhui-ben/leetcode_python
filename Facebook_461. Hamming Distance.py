#461. Hamming Distance

#The Hamming distance between two integers is the number of positions 
#at which the corresponding bits are different.

#Given two integers x and y, calculate the Hamming distance.

#Note:
#0 ≤ x, y < 231.

#Example:

#Input: x = 1, y = 4

#Output: 2

#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#       ↑   ↑

#The above arrows point to positions where the corresponding bits are different.


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        while x>0 or y>0:
            ans+= x%2 ^ y%2 ## XOR operation
            x=x//2
            y=y//2
        return ans
        
        ## brute force
#         def to_binary(x):
#             if x==0:return '0'
#             elif x==1:return '1'
#             else: return to_binary(x//2)+ str(x%2)
#         binary_x, binary_y= to_binary(x), to_binary(y)
#         dif= abs(len(binary_x)-len(binary_y))
#         if len(binary_x)> len(binary_y):
#             binary_y="0" * dif+binary_y
#         else:
#             binary_x="0" * dif+binary_x
#         ans=0
#         for i in range(len(binary_x)):
#             if binary_x[i]!=binary_y[i]:
#                 ans+=1
                
#         return ans
