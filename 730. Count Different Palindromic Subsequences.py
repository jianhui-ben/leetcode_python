#730. Count Different Palindromic Subsequences
#Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

#A subsequence of a string is obtained by deleting zero or more characters from the string.

#A sequence is palindromic if it is equal to the sequence reversed.

#Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

# Example 1:

#Input: s = "bccb"
#Output: 6
#Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
#Note that 'bcb' is counted only once, even though it occurs twice.

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """
        1、计算单个字符
        2、计算 a*a, b*b, c*c, d*d, 其中 * 表示 空字符串 或者 对称字符串
        因此，分别找到 最左边 和 最右边 的字符，递归调用 计算内部字符串 的对称字符串个数， 考虑到还有空字符串， 还需要额外 +1
        """
        self.mem = {}
        
        def recursion(s, start, end):
            
            count = 0
            if (start, end) in self.mem:
                return self.mem[(start, end)]

            for ele in 'abcd':
                if ele in s[start: end + 1]:
                    count += 1
            
            for ele in 'abcd':
                left, right = s[start: end + 1].find(ele), s[start: end + 1].rfind(ele)
                if left > -1 and right > -1 and right > left:
                    count += recursion(s, start + left + 1, start + right - 1) + 1
                
            self.mem[(start, end)] = count % (10**9 + 7)
            return self.mem[(start, end)]
        
        return recursion(s, 0, len(s)-1)
        