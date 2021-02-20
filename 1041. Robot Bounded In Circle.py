#1041. Robot Bounded In Circle
#On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

#"G": go straight 1 unit;
#"L": turn 90 degrees to the left;
#"R": turn 90 degrees to the right.
#The robot performs the instructions given in order, and repeats them forever.

#Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ## typical diverging trajectory VS limit cycle trjectory
        ## if the robot return to 00 or not facing 
        
        # north = 0, east = 1, south = 2, west = 3
        directions =[[0, 1], [1, 0], [0, -1], [-1, 0]]
        x,y=0,0
        cur_dir= 0
        for i in instructions:
            if i== 'G':
                x+= directions[cur_dir][0]
                y+= directions[cur_dir][1]
                
            elif i== 'R':
                cur_dir= (cur_dir+1)%4
            else:
                cur_dir= (cur_dir+3)%4
            
        return (x==0 and y==0) or (cur_dir!=0)
        
        