#241. Different Ways to Add Parentheses
#Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

#Example 1:

#Input: "2-1-1"
#Output: [0, 2]
#Explanation: 
#((2-1)-1) = 0 
#(2-(1-1)) = 2


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ## split the input
        l=[]
        new_num=True
        for i in input:
            if i.isdigit():
                if new_num:
                    l.append(int(i))
                    new_num=False
                else:
                    k=l.pop()
                    l.append(k*10+ int(i))
            else:
                l.append(i)
                new_num=True
        return self.computeList(l)
    
    def computeList(self, l):
        def compute(num1, num2, op):
            if op=='+':
                return num1+num2
            elif op=='-':
                return num1-num2
            else:
                return num1*num2

        if not l: return None
        if len(l)==1:
            return [l[0]]
        if len(l)==3:
            return [compute(l[0], l[2], l[1])]
        out=[]
        for i in range(1, len(l)-1, 2):
            left= self.computeList(l[:i])
            right=self.computeList(l[i+1:])
            for left_num in left:
                for right_num in right:
                    out.append(compute(left_num, right_num, l[i]))
        return out