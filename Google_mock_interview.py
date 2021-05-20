# 2 questions in https://www.youtube.com/watch?v=rw4s4M3hFfs&t=761s
## google coding interview

def bestBlocks(blocks, req):
    ## for each req, we need to have the min dis from blocks[i] to achieve req
    ## we use two pass (left to right and then right to left)
    
    ## gym: false, true, true, false, false
    ## left to right: inf, 0, 0, 1, 2
    ## right to left: 1, 0, 0 , inf,inf
    ## combine: 1, 0, 0, 1,2
    
    ## O(len(blocks) * len(r)) time, O(len(blocks)) space
    def traverse(blocks, r):
        res=[None] * len(blocks)
        for i in range(len(blocks)):
            if blocks[i][r]:
                res[i] =  0
            elif i>0 and res[i-1]!= float('inf'):
                res[i] = res[i-1]+1
            else:
                res[i] =float('inf')
        return res
                
    combine = [0] * len(blocks)
    for r in req:
        left_to_right = traverse(blocks, r)
        right_to_left = traverse(blocks[::-1], r)[::-1]
        
        for i in range(len(left_to_right)):
            combine[i] =  max(combine[i], min(left_to_right[i], right_to_left[i]))
        
    return combine.index(max(combine))


def longestBuildRun(builds):
    ## compress the builds to a list
    green_percent = [float(sum(l))/float(len(l)) for l in builds]
    ## 0.8, 0.9, 0.2, 0.1, 0.4
    ## 1, 1, 2,3,1
    res, temp_count, temp_percent =  1, 1, green_percent[0]
    for i in range(1, len(green_percent)):
        if green_percent[i]>= temp_percent:
            temp_count =1
        else:
            temp_count+=1
            res = max(res, temp_count)
        temp_percent = green_percent[i]
        
    return res
        
    
        
    
    
