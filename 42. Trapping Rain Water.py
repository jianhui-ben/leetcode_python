#42. Trapping Rain Water
#Given n non-negative integers representing an elevation map where the width of each bar is 1, 
#compute how much water it can trap after raining.
class Solution:
    def trap(self, height: List[int]) -> int:
        ## two pointer
        ## O(n), space O(1)
        left, right= 0, len(height)-1
        leftmax, rightmax=0, 0 
        out=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    out+= leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    out+=rightmax-height[right]
                right-=1
        return out
                    
        
        
        
        
        
        ## dynamic programming:
        ##time O(n), space O(n)
        left_max=0
        left=[]
        for i in range(len(height)):
            left_max= max(left_max, height[i])
            left.append(left_max)
        right_max=0
        right=[]
        for i in range(len(height)-1, -1, -1):
            right_max= max(right_max, height[i])
            right.append(right_max)
        right=right[::-1]
        out=0
        for i in range(len(height)):
            out+=min(right[i], left[i])-height[i]
            
        return out
        
        
        
        
        
        ## two pointer
#         if len(height)<3: return 0
        
        
        
        
        
#         ## use the stack
        
#         if len(height)<3: return 0
#         start, end= 0, len(height)-1
        
#         while start+1<len(height) and height[start+1]>=height[start]:
#             start+=1
#         while end-1>=0 and height[end-1]>=height[end]:
#             end-=1
#         out= 0
#         print(start, end)
#         if end-start>1:
#             stack=[height[start]]
#             for i in range(start, end+1):
#                 if height[i]<stack[-1]:
#                     stack.append(height[i])
#                 else:
#                     h= min(stack[0], height[i])
#                     while stack and height[i]>=stack[-1]:
#                         last=stack.pop()
#                         out+= h-last
#                     stack.append(height[i])
#                 print(stack, out)
#         return out
                
            

            
            
                
        
        
        
        
        
        
        
        
        
        
        ## first traverse to get the interval of the trap
        ## then get how much water in each interval
        
#         if len(height)<3: return 0
#         start, end= 1, len(height)-2
        
#         while start<len(height) and height[start]>=height[start-1]:
#             start+=1
#         while end>=0 and height[end]>=height[end+1]:
#             end-=1
#         out=0
#         def area(height, left, right):
#             h= min(height[left], height[right])
#             return sum([max(h-i, 0) for i in height[left: right+1]])
        
#         start-=1
#         end+=1
#         print(start, end)

#         while start<end:
#             left=start
#             while start+1<=end and height[start+1]<height[start]:
#                 start+=1
#             while start+1<=end and height[start+1]>=height[start]:
#                 start+=1
            
#             if left< start:
#                 out+= area(height, left, start)
#             print(left, start)

#         return out