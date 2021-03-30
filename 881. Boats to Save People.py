#881. Boats to Save People
#You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

#Return the minimum number of boats to carry every given person.

 

#Example 1:

#Input: people = [1,2], limit = 3
#Output: 1
#Explanation: 1 boat (1, 2)


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ## two pointer
        ## time O(nlogn), space O(n)
        people.sort()
        left, right= 0, len(people)-1
        count=0
        while left<=right:
            count+=1
            if people[right]+ people[left]<=limit:
                right-=1
                left+=1
            else:
                right-=1
        
        return count