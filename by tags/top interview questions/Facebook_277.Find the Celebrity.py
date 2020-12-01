#277.Find the Celebrity

#Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, 
#there may exist one celebrity. The definition of a celebrity is 
#that all the other n - 1 people know him/her but he/she does not know any of them.

#Now you want to find out who the celebrity is or verify that there is not one. 
#The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" 
#to get information of whether A knows B. You need to find out the celebrity 
#(or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

#You are given a helper function bool knows(a, b) which tells you whether 
#A knows B. Implement a function int findCelebrity(n), your function should 
#minimize the number of calls to knows.


#Example1

#Input:
#2 // next n * (n - 1) lines 
#0 knows 1
#1 does not know 0
#Output: 1
#Explanation:
#Everyone knows 1,and 1 knows no one.


"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        if n==0: return -1
        if n==1: return 0
        people= [i for i in range(n)]
        while people:
            if len(people)==1: break
            if Celebrity.knows(people[0], people[1]) and Celebrity.knows(people[1], people[0]):
                people= people[2:]
            elif Celebrity.knows(people[0], people[1]):
                people.pop(0)
            elif Celebrity.knows(people[1], people[0]):
                people.pop(1)
            else:
                people= people[2:]
        if len(people)==0: return -1
        last_option= people[0]
        for k in range(n):
            if k!=last_option:
                if Celebrity.knows(last_option, k) or not Celebrity.knows(k, last_option):
                    return -1
        return last_option