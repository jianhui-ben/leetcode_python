#735. Asteroid Collision

#We are given an array asteroids of integers representing asteroids in a row.

#For each asteroid, the absolute value represents its size, and the sign represents
#its direction (positive meaning right, negative meaning left). Each asteroid moves 
#at the same speed.

#Find out the state of the asteroids after all collisions. If two asteroids meet, 
#the smaller one will explode. If both are the same size, both will explode. Two 
#asteroids moving in the same direction will never meet.

 

#Example 1:

#Input: asteroids = [5,10,-5]
#Output: [5,10]
#Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
#Example 2:

#Input: asteroids = [8,-8]
#Output: []
#Explanation: The 8 and -8 collide exploding each other.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ##better method:
        out=[]
        for star in asteroids:
            while out and out[-1]>0 and star<0:
                if abs(out[-1])>abs(star):
                    break
                elif abs(out[-1])<abs(star):
                    out.pop()
                elif abs(out[-1])==abs(star):
                    out.pop()
                    break
            else:
                out.append(star)
        
        return out
                     
        
#         ##Ben's method
#         positive=False
#         temp=[]
#         add_negative=True
#         for i in range(len(asteroids)):
#             if asteroids[i] < 0 and not positive:
#                 temp.append(asteroids[i])
#             elif asteroids[i]>=0:
#                 positive=True
#                 temp.append(asteroids[i])
#             elif asteroids[i]<0 and positive:
#                 while len(temp)>0 and temp[-1]>0:
#                     last_positive=temp.pop()
#                     if last_positive+ asteroids[i]>0:
#                         temp.append(last_positive)
#                         break
#                     elif last_positive+ asteroids[i]==0:
#                         add_negative=False
#                         break
                        
#                 if (len(temp)==0 or temp[-1]<=0) and add_negative: temp.append(asteroids[i])
#                 add_negative=True
#                 if not temp: positive=False
#                 else: positive= temp[-1]>=0
#                 add_negative=True
#         return temp
