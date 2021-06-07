#990. Satisfiability of Equality Equations
#Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

#Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

#Example 1:

#Input: ["a==b","b!=a"]
#Output: false
#Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.


# class uf:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.size = [1]*n
    
#     def union(self, x, y):
#         x_root = self.find(x)
#         y_root = self.find(y)
#         if x_root ==y_root: return
#         if self.size[x_root]>=self.size[y_root]:
#             self.parent[y_root] = x_root
#             self.size[x_root]+= self.size[y_root]
#         else:
#             self.parent[x_root] = y_root
#             self.size[y_root]+= self.size[x_root]
        
#     def find(self, x):
#         while self.parent[x]!=x:
#             self.parent[x]= self.parent[self.parent[x]]
#             x=self.parent[x]
#         return x
    
#     def connected(self, x, y):
#         return self.find(x)==self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ## union find O(n)
        
        def find(parent, a):
            while parent[a]!=a:
                a=parent[a]
            return a            
        
        def union(parent, a, b):
            a_root= find(parent, a)
            b_root = find(parent, b)
            if a==b: return
            parent[a_root]= b_root
        
        parent = defaultdict()
        for i in equations:
            parent[i[0]]=i[0]
            parent[i[3]]=i[3]
        
        for i in equations:
            if i[1]=='=':
                union(parent, i[0], i[3])
        for i in equations:
            if i[1]=='!' and find(parent, i[0])==find(parent, i[3]):
                return False
            
        return True
        


