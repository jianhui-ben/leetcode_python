#1152. Analyze User Website Visit Pattern

#We are given some website visits: the user with name username[i] visited the
#website website[i] at time timestamp[i].

#A 3-sequence is a list of websites of length 3 sorted in ascending order by 
#the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

#Find the 3-sequence visited by the largest number of users. If there is more
#than one solution, return the lexicographically smallest such 3-sequence.

 

#Example 1:

#Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
#Output: ["home","about","career"]
#Explanation: 
#The tuples in this example are:
#["joe", 1, "home"]
#["joe", 2, "about"]
#["joe", 3, "career"]
#["james", 4, "home"]
#["james", 5, "cart"]
#["james", 6, "maps"]
#["james", 7, "home"]
#["mary", 8, "home"]
#["mary", 9, "about"]
#["mary", 10, "career"]
#The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
#The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
#The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
#The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
#The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.

class Solution:
    
    ##dfs helper function
    def three_sequences(self, webs):
        out=set()
        def dfs(i, cur_3):
            if len(cur_3)==3:
                out.add(" ".join(list(cur_3)))
            elif i<len(webs):
                dfs(i+1, cur_3)
                dfs(i+1, cur_3+[webs[i]])
        dfs(0, [])
        return out

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        ##brute force
        ##be careful: the time can be non-consecutive
        records=[]
        for _, user, web in sorted(zip(timestamp, username, website),key=lambda item:item[0]):
            records.append((user, web))
        
        user_webs={}
        for user, web in records:
            if user not in user_webs:
                user_webs[user]=[web]
            else:
                user_webs[user].append(web)

        webs_users={}
        for user, webs in user_webs.items():
            for three_seq in self.three_sequences(webs):
                if three_seq not in webs_users:
                    webs_users[three_seq]=set([user])
                else:
                    webs_users[three_seq].add(user)
        return sorted(webs_users.items(), key=lambda item: (-len(item[1]),item[0]))[0][0].split()
            
            
        
            
