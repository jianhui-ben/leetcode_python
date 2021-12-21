# 902. Numbers At Most N Given Digit Set
# Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
#
# Return the number of positive integers that can be generated that are less than or equal to a given integer n.
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
        dp
        given a int n--> str_n
        dp[i] = # of valid number with len(str_n) - idigits and smaller or equal to str_n[i:]

        """

        str_n, cnt_digits = str(n), len(digits)
        dp = [0] * len(str_n) + [1]
        for i in range(len(str_n) - 1, -1, -1):

            for digit in digits:
                if int(digit) < int(str_n[i]):
                    dp[i] += cnt_digits ** (len(str_n) - i - 1)
                elif int(digit) == int(str_n[i]):
                    dp[i] += dp[i + 1]

        out = 0

        for i in range(1, len(str_n)):
            out += cnt_digits ** i

        return dp[0] + out