# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

def permute(nums):
    out = []

    def backtrack(cur, left):
        if not left:
            out.append(cur[:])
            return
        available = list(left)
        for i in available:
            left.remove(i)
            cur.append(i)
            backtrack(cur, left)
            cur.pop()
            left.add(i)
    backtrack([], set(nums))

    return out

print(permute([1,2,3, 5]))