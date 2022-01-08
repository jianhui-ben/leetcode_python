"""
Given an array A of length n, you take k numbers either from the beginning or the end, each number taken is removed from the array. What's the maximum sum of the numbers taken?
e.g. A = [1,3,1,2,3,1], k = 4, output is 8

we want to minimize sum(A[i:j]) where i + len(A) - j == k, len(A) > k, --> j - i = len(A) - k
A[3: 5]
len(A) = 6
k = 4


brute force: get all the sum of A[i:j] -> O(n**2)

sliding windown: O(n) where j > i and A[i:j] is valid,
if the dis between i and j < len(A) - k, add the current number
if the dis == len(A)-k, we min(res, current sum), and - nums[i], i++

"""


def maxSumTaken(nums, k):
    """
    [1], k=0, res = 0

    [prefix sum....            ....suffix sum]


    k....... k

    2K numbers into a new arr

    time: O(K); space: O(1)
    """
    res = float('inf')
    i, j, cur_sum = 0, 0, 0
    while j < len(nums):
        cur_sum += nums[j]
        j += 1
        if j - i == len(nums) - k:
            res = min(res, cur_sum)
            cur_sum -= nums[i]
            i += 1

    return sum(nums) - res

