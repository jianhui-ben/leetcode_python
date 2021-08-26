#859. Buddy Strings

#Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

#Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

#For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

#Example 1:

#Input: s = "ab", goal = "ba"
#Output: true
#Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            visited = set() ## this set will have max length = 26

            for i in range(len(s)):
                if s[i] in visited:
                    return True

                visited.add(s[i])

            return False

        ## when s != goal

        cnt_off, val_off = 0, [None] * 2

        for i in range(len(s)):

            if s[i] != goal[i] and not cnt_off:
                cnt_off += 1
                val_off[0] = s[i]
                val_off[1] = goal[i]
            elif s[i] != goal[i]:
                cnt_off += 1
                if val_off[1] != s[i] or val_off[0] != goal[i]:
                    return False
                
            if cnt_off > 2:
                return False

        if cnt_off == 2 and len(val_off) == 2:
            return True

        return False
