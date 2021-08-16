#163. Missing Ranges
#You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

#A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

#Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

#Each range [a,b] in the list should be output as:

#"a->b" if a != b
#"a" if a == b
 

#Example 1:

#Input: nums = [0,1,3,50,75], lower = 0, upper = 99
#Output: ["2","4->49","51->74","76->99"]
#Explanation: The ranges are:
#[2,2] --> "2"
#[4,49] --> "4->49"
#[51,74] --> "51->74"
#[76,99] --> "76->99"


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        """
        nums = [0,1,3,50,75], lower = 0, upper = 99
        
        cur_lower = 0, cur_i = 0
        
        for every cur_i in len(nums):
            if nums[cur_i] == cur_lower --> cur_lower += 1
            if nums[cur_i] - 1 > cur_lower: append(cur_lower -->nums[cur_i] - 1 )
            if nums[cur_i] - 1 == cur_lower: append(cur_lower)
        
        lastly, you check with the upper
        time: O(n)
        space: O(1)
        """
        out = []
        cur_low = lower
        for num in nums:
            if num == cur_low:
                cur_low = num + 1
                continue
            
            if num - 1 == cur_low:
                out.append(str(cur_low))
            else:
                out.append(str(cur_low) + '->' + str(num - 1))
            cur_low = num + 1
        
        if upper == cur_low:
            out.append(str(upper))
        elif upper > cur_low:
            out.append(str(cur_low) + '->' + str(upper))
        
        return out
                
        
        