# 790. Domino and Tromino Tiling
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
#
#
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
#
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

class Solution:
    def numTilings(self, n: int) -> int:
        """
        dp
        two conditions: full cover or partial covered f(k) and p(k)
        f[k] = f[k - 1] + f[k - 2] + 2 * p[k - 1]
        p[k - 1] = f[k - 2] + p[k - 1]
        base case:
        f[0] = 1, f[1] = 1
        p[0], p[1] = 0

        f[2] = 2
        p[2] = 1


        f[3] = 2 + 1 + 2 *1
        p[3] = 1 + 1 = 2

        """
        f, p = [1, 1], [0, 0]
        for k in range(2, n + 1):
            temp_f, temp_p = [None] * 2, [None] * 2
            temp_f[0], temp_p[0] = f[1], p[1]
            temp_f[1] = (f[1] + f[0] + 2 * p[1]) % (10 ** 9 + 7)
            temp_p[1] = (f[0] + p[1]) % (10 ** 9 + 7)
            f, p = temp_f, temp_p

        return f[-1]









