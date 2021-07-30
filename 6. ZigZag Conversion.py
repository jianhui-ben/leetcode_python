#6. ZigZag Conversion
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"

#Write the code that will take a string and make this conversion given a number of rows:

#string convert(string s, int numRows);
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        O(n), O(n)
        """
        if numRows == 1: return s
        
        stored = [''] * numRows
        
        goUp = False
        
        def traverse(cur_row, idx, goUp):
            nonlocal s, numRows
            if idx == len(s): return
            stored[cur_row] += s[idx]
            
            if not goUp:
                if cur_row + 1 < numRows:
                    traverse(cur_row + 1, idx + 1, False)
                else:
                    traverse(cur_row - 1, idx + 1, True)
            else:
                if cur_row - 1 >= 0:
                    traverse(cur_row - 1, idx + 1, True)
                else:
                    traverse(cur_row + 1, idx + 1, False)

        traverse(0, 0, goUp)
        
        return ''.join(stored)