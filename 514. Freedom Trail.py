#514. Freedom Trail
#In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

#Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

#Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

#At the stage of rotating the ring to spell the key character key[i]:

#You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
#If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
    ## dp: status: ring r, index of key i
    ## choice= rotate clockwise or anti or not press
    ## dp function return the min number of ations needed to get from ring to key[i:]
    ## dp(r, i):
    ## if i==len(key): return 0
    ## if r[0]==key[i]: dp(r, i+1)+1
    ## else: min(dp(clockwise, i), dp(anti, i))
    ## O(len(ring)*len(key)* len(ring/2)), space O(len(ring)*len(key))
    
        def rotate(cur_ring, target, if_clock):
            ## return # of steps of rotating cur_ring to make cur_ring[0]==target
            step=0
            while cur_ring[0]!=target:
                if if_clock:
                    cur_ring=cur_ring[1:]+cur_ring[0]
                else:
                    cur_ring=cur_ring[-1]+cur_ring[:-1]
                step+=1
            return step, cur_ring
                

        
        def recursion(ring, key, cur_ring, cur_key_i):
            if cur_key_i==len(key):
                return 0
            if (cur_ring, cur_key_i) in self.mem:
                return self.mem[(cur_ring, cur_key_i)]
            if cur_ring[0]==key[cur_key_i]: 
                return 1+recursion(ring, key, cur_ring, cur_key_i+1)
            else:
                clock_step, clock_ring= rotate(cur_ring, key[cur_key_i], True)
                anti_clock_step,anti_clock_ring=rotate(cur_ring, key[cur_key_i],False)
                
                res = min(clock_step+ recursion(ring, key, clock_ring, cur_key_i),
                anti_clock_step+ recursion(ring, key, anti_clock_ring, cur_key_i))
                self.mem[(cur_ring, cur_key_i)] = res
            return self.mem[(cur_ring, cur_key_i)]
            
        self.mem = defaultdict()
        return recursion(ring, key, ring, 0)
    
    
        