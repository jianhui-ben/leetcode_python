#97. Interleaving String


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ## dynamics programming
        ## status: i1, i2, i3
        ## choice: we increment i1 or i2
        
        ## top down recursion O(m*n), space O(m*n)
        self.mem = defaultdict()
        
        def helper(i1,i2,i3):
            nonlocal s1, s2, s3            
            if i1==len(s1):
                return s2[i2:]==s3[i3:]
            elif i2==len(s2):
                return s1[i1:]==s3[i3:]
            elif i3==len(s3):
                return False
            elif (i1,i2,i3) in self.mem:
                return self.mem[(i1,i2,i3)]
            else:
                self.mem[(i1,i2,i3)] = (s1[i1]==s3[i3] and helper(i1+1, i2, i3+1)) \
                                        or (s2[i2]==s3[i3] and helper(i1, i2+1, i3+1))
            return self.mem[(i1,i2,i3)] 
        
