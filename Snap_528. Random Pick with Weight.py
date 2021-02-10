#528. Random Pick with Weight
#You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

#We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

#More formally, the probability of picking index i is w[i] / sum(w).

class Solution:
    ## random choice
    def __init__(self, w: List[int]):
        self.population= list(range(len(w)))
        self.weights=w

    def pickIndex(self) -> int:
        import random
        return random.choices(self.population, self.weights)[0]

    ##brute force
#     def __init__(self, w: List[int]):
#         array= []
#         for i, cnts in enumerate(w):
#             for k in range(cnts):
#                 array.append(i)
#         self.array=array

#     def pickIndex(self) -> int:
#         import random
#         return self.array[random.randint(0, len(self.array)-1)]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
