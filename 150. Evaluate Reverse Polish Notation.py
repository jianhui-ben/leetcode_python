#150. Evaluate Reverse Polish Notation
#Evaluate the value of an arithmetic expression in Reverse Polish Notation.

#Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

#Note that division between two integers should truncate toward zero.

#It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        save into a stack, 
        as long as we see the operator, we pop out last two number
        calculate the result and push back to the top of the stack
        """
        stack = []
        
        for i in tokens:
            if i not in set(['-', '+', '*', '/']):
                stack.append(int(i))
            else:
                second, first = stack.pop(), stack.pop()
                if i == '+':
                    res = first + second
                elif i == '-':
                    res = first - second
                elif i == '*':
                    res = first * second
                else:
                    ## need to be careful about the truncate to zero division
                    res = int(first / second)
                stack.append(res)
        #["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
            # print(stack)
        return stack[0]
            