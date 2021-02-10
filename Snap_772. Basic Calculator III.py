#772. Basic Calculator III
#Implement a basic calculator to evaluate a simple expression string.

#The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

#You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

#Follow up: Could you solve the problem without using built-in library functions.

 

#Example 1:

#Input: s = "2*(5+5*2)/3+(6/2+8)"
#Output: 21



class Solution:

    def compute(self, last1,last2, op):
        if op =='+': return last1+last2
        elif op=='-': return last2-last1
        elif op=='*': return last2*last1
        else: return last2//last1


    def calculate(self, s: str) -> int:

        operands, operators= [], []
        new_num, order=True, 0
        for i in s:
            if i==" ": pass
            elif i.isdigit():
                if new_num:
                    operands.append(int(i))
                    new_num=False
                else:
                    x=operands.pop()
                    operands.append(x*10+int(i))
            elif i=="(":
                new_num=True
                order+=2
            elif i==")":
                new_num=True
                order-=2
            else:
                new_num=True
                if i=="-" and not operands:
                    operands.append(0)
                    operators.append((i, order+3))
                    pass
                elif i=="+" or i=="-":
                    cur_order=0
                else:
                    cur_order=1
                while operators and order+cur_order<=operators[-1][1]:
                    last1,last2= operands.pop(), operands.pop()
                    op, _=operators.pop()
                    operands.append(self.compute(last1,last2, op))    
                operators.append((i, order+cur_order))
        while operators:
            last1,last2= operands.pop(), operands.pop()
            op, _=operators.pop()
            operands.append(self.compute(last1,last2, op)) 
        
        return operands[-1]