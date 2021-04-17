#301. Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ## BFS to determine the min # of removal
        
        queue =[s]
        visited =set([s])
        step= 0
        out=[]
        stop=False
        
        def is_valid(i):
            ## using stack
            stack=[]
            for c in i:
                if c=='(':
                    stack.append(c)
                elif c==')' and not stack:
                    return False
                elif c==')':
                    stack.pop()
                else:
                    continue
            return len(stack)==0
        
        def make_change(i, visited):
            temp_out=[]
            for idx in range(len(i)):
                if i[idx]!= '(' and i[idx]!= ')':
                    continue
                else:
                    new_s = i[:idx]+i[idx+1:]
                    if new_s not in visited:
                        temp_out.append(new_s)
                        visited.add(new_s)
            return temp_out

        
        
        while queue:
            temp=[]
            for i in queue:
                if is_valid(i):
                    out.append(i)
                    stop=True
                else:
                    temp=temp+make_change(i, visited)
            if stop: return out
            step+=1
            queue= temp
            
        return out
                    
        
