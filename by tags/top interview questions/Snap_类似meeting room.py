# 类似meeting room: given n person's meeting schedule, find all time slots that all these n person could be available (not in any meeting)


nums=[[0,2],[5,10],[15,20], [1,3], [4, 6]]
# out=[[2,5], [10, 15]]

def all_available(nums):
    ## two pointers
    out=[]
    nums.sort(key= lambda x: x[0])
    lower=nums[0][1]
    
    for start, end in nums[1:]:
        if start> lower:
            out.append([lower,start])
        lower= end
    return out
    
print(all_available(nums)) 
