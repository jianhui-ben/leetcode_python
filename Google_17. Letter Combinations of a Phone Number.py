#17. Letter Combinations of a Phone Number

#Given a string containing digits from 2-9 inclusive, return all possible letter 
#combinations that the number could represent. Return the answer in any order.

#A mapping of digit to letters (just like on the telephone buttons) is 
#given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ##brute force: Ben's method
        # stored={'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno'\
        #        , '7':'pqrs', '8':'tuv', '9':'wxyz'}
        # if not digits: return []
        # out= [""]
        # for digit in digits:
        #     letters= stored[digit]
        #     temp=[]
        #     for l in letters:
        #         for sub in out:
        #             temp.append(sub+l)
        #     out= temp
        # return out
    
        ##backtracking + recursion:
        ##time complexity: O(3**N + 4**M) where N is # of digits for 3 letters and M is #
        ## of digits for 4 letters

        stored={'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno'\
               , '7':'pqrs', '8':'tuv', '9':'wxyz'}
        out=[]
        if not digits: return []
        def backtrack(combo, digits):
            if len(digits)==0:
                out.append(combo)
            else:
                for letter in stored[digits[0]]:
                    backtrack(combo+letter, digits[1:])

        backtrack("", digits)
        return out   
                    




        
        
        
