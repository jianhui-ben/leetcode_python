
#496. Next Greater Element I
#You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

#Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

#The Next Greater Number of a number x in nums1 is the first greater 
#to its right in nums2. If it does not exist, return -1 for this number.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## perfect question for monotonous stack
        ## O(n), O(n)
        next_great = defaultdict()
        stack = []
        for i in range(len(nums2)-1, -1, -1):  ## backward to add into stack
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if not stack:
                next_great[nums2[i]] = -1
            else:
                next_great[nums2[i]] = stack[-1]
            
            stack.append(nums2[i])
        
        return [next_great[i] for i in nums1]  
        
#         ## brute force O(n*m), O(n)
        
#         out= []
#         for i1 in nums1:
#             index_2 = nums2.index(i1)
#             temp =float('inf')
            
#             for i2 in nums2[index_2+1: ]:
#                 if i2>i1 and i2<temp:
#                     temp = i2
#                     break
#             if temp!= float('inf'):
#                 out.append(temp)
#             else:
#                 out.append(-1)
                
#         return out
        