#Shuffle a set of numbers without duplicates.

#Example:

#// Init an array with set 1, 2, and 3.
#int[] nums = {1,2,3};
#Solution solution = new Solution(nums);

#// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
#solution.shuffle();

#// Resets the array back to its original configuration [1,2,3].
#solution.reset();

#// Returns the random shuffling of array [1,2,3].
#solution.shuffle();

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        a= list(set(self.nums))
        random.shuffle(a)
        return a
    """
    Method 2:
class Solution:Fisher-Yates Algorithm
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
    """


