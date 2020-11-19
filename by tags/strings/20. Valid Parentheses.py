#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

#Example 1:

#Input: "()"
#Output: true
#Example 2:

#Input: "()[]{}"
#Output: true



## using a stack: time O(n); space O(n)
def isValid(s: str) -> bool:
    if len(s)%2!=0:
        return False
    dic={'(':')', '{':'}', '[':']'}
    queue= []
    for i in s:
        if i in dic.keys():
            queue.append(i)
        else:
            if len(queue)>0:
                if i!= dic[queue[-1]]:
                    return False
                else:
                    queue.pop()
            else:
                return False
    if len(queue)==0:
        return True
    return False

   

##test case:
s1= '([)]'
s2= "{[]}"
isValid(s1)
isValid(s2)

