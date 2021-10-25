# 1569. Number of Ways to Reorder Array to Get Same BST
# Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.
#
# For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
#
# Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.
#
# Since the answer may be very large, return it modulo 10^9 + 7.

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        """
        recursion helper(nums)

        left_nums: part of nums for the left part
        right_nums: part of nums for right part
        root: nums[0]

        if both greater than 0:
        return (helper(left_nums)) *
                (helper(right_nums)) * 2
        else: return the non-zero result

        return helper(nums) - 1


        base case of helper():
        if len(nums) == 0: return 0
        if len(nums) < 3: return 1

        """

        def helper(nums):
            if len(nums) < 2: return 1
            left, right = [], []
            for i in range(1, len(nums)):
                if nums[i] < nums[0]:
                    left.append(nums[i])
                elif nums[i] > nums[0]:
                    right.append(nums[i])
            return comb(len(left) + len(right), len(left)) * helper(left) * helper(right)

        return (helper(nums) - 1) % (10 ** 9 + 7)






