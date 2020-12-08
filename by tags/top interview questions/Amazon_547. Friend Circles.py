#547. Friend Circles
#There are N students in a class. Some of them are friends, 
#while some are not. Their friendship is transitive in nature. 
#For example, if A is a direct friend of B, and B is a direct friend
#of C, then A is an indirect friend of C. And we defined a friend circle 
#is a group of students who are direct or indirect friends.

#Given a N*N matrix M representing the friend relationship between students
#in the class. If M[i][j] = 1, then the ith and jth students are direct 
#friends with each other, otherwise not. And you have to output the total 
#number of friend circles among all the students.

#Example 1:

#Input: 
#[[1,1,0],
# [1,1,0],
# [0,0,1]]
#Output: 2
#Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
#The 2nd student himself is in a friend circle. So return 2.

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        if not M: return 0
        groups= dict()
        group_index= 0
        for i in range(len(M)):
            temp=[]
            if str(i) in groups:
                continue
            else:
                groups[str(i)]= group_index
                temp= [index for index, k in enumerate(M[i]) if k==1]
            while temp:
                friend= temp.pop()
                if str(friend) not in groups:
                    groups[str(friend)]= group_index
                    temp+= [index for index, k in enumerate(M[friend]) if k==1 and str(index) not in groups]
            group_index+=1
        # return groups
        return len(set(groups.values()))     
                        
            