
#169. Majority Element
#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

#You may assume that the array is non-empty and the majority element always exist in the array.

#Example 1:

#Input: [3,2,3]
#Output: 3
#Example 2:

#Input: [2,2,1,1,1,2,2]
#Output: 2

class Solution:
    ## use python dict/ hashtable
    def majorityElement(self, nums: List[int]) -> int:
        dic= {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else: dic[i]=1
        print(dic)
        return sorted(dic.items(),  key=lambda x: x[1] )[-1][0]
