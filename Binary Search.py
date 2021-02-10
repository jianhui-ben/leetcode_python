
#There’re 2 ways to implement the simplest binary search on a sorted array:
def binary_search(nums, lo, hi, target):
    if lo > hi:
        return lo
    mid = (lo+hi)//2
    if nums[mid] == target:
        return mid
    else:
        return binary_search(nums, mid+1, hi, target) if nums[mid] < target else binary_search(nums, lo, mid-1, target)

def binary_search_stack(nums, target):
    lo, hi = 0, len(nums)-1
    while lo < hi: # since it's array, we don't need to use while True to keep it loop
        mid = (lo+hi)//2
        if nums[mid] == target:
            lo = mid
            break
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


