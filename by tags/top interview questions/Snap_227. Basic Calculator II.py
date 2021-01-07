#227. Basic Calculator II

#Given a string s which represents an expression, evaluate this expression and return its value. 

#The integer division should truncate toward zero.

 

#Example 1:

#Input: s = "3+2*2"
#Output: 7

class Solution:
    def compute(self, last1,last2, op):
        if op =='+': return last1+last2
        elif op=='-': return last2-last1
        elif op=='*': return last2*last1
        else: return last2//last1
    
    
    def calculate(self, s: str) -> int:
        ##we will do * and / first in two stacks
        operands, operators= [], []
        new_num=True
        for i in s:
            if i==" ": pass
            elif i.isdigit():
                if new_num:
                    operands.append(int(i))
                    new_num=False
                else:
                    x=operands.pop()
                    operands.append(x*10+int(i))
            else:
                new_num=True
                if not operands: operands
                if i=="+" or i=="-":
                    order=0
                else:
                    order=1
                while operators and order<=operators[-1][1]:
                    last1,last2= operands.pop(), operands.pop()
                    op, _=operators.pop()
                    operands.append(self.compute(last1,last2, op))    
                operators.append((i, order))
                
        while operators:
            last1,last2= operands.pop(), operands.pop()
            op, _=operators.pop()
            operands.append(self.compute(last1,last2, op))
        return operands[-1]
                    
