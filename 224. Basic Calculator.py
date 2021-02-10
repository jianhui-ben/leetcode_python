#224. Basic Calculator
#Given a string s representing an expression, implement a basic calculator to evaluate it.

 

#Example 1:

#Input: s = "1 + 1"
#Output: 2


class Solution:
    def calculate(self, s: str) -> int:
        operators, operands=[], []
        order=0
        new_num= True
        for i in s:
            if i==' ': pass
            elif i.isdigit():
                if new_num: 
                    operands.append(int(i))
                    new_num=False
                else:
                    x=operands.pop()
                    operands.append(10*x+ int(i))
            elif i=='(':
                order+=1
                new_num=True
            elif i==")":
                order-=1
                new_num=True
            else:
                if not operands: operands.append(0)
                new_num=True
                while operators and order<=operators[-1][1]:
                    last1,last2= operands.pop(), operands.pop()
                    op, _= operators.pop()
                    if op=='+': 
                        operands.append(last1+last2)
                    else: operands.append(last2-last1)
                operators.append((i, order))

        # print(operands)
        # print(operators)
        while operators:
            last1,last2= operands.pop(), operands.pop()
            op, _= operators.pop()
            if op=='+': 
                operands.append(last1+last2)
            else: operands.append(last2-last1)
                
        return operands[-1]