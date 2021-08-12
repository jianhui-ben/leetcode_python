#954. Array of Doubled Pairs

#Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

 

#Example 1:

#Input: arr = [3,1,3,6]
#Output: false
#Example 2:

#Input: arr = [2,1,2,6]
#Output: false
#Example 3:

#Input: arr = [4,-2,2,-4]
#Output: true
#Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
#Example 4:

#Input: arr = [1,2,4,16,8,4]
#Output: false

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        """
        arr[1] = 2* arr[0]
        arr[3] = 2 * arr[2]
        arr[5] = 2 * arr[4]
        ...
        
        sort the counter
        """
        stored = collections.Counter(arr)
        for val in sorted(stored):
            if stored[val] == 0:
                continue
            if val < 0:
                if val % 2 or val // 2 not in stored or stored[val // 2] < stored[val]:
                    return False
                else:
                    stored[val // 2] -= stored[val]
            elif val > 0:
                if val * 2 not in stored or stored[val * 2] < stored[val]:
                    return False
                else:
                    stored[val * 2] -= stored[val]
            elif stored[val] % 2:
                return False
        
        return True
        
