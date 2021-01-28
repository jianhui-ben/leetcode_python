#986. Interval List Intersections

#You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

#Return the intersection of these two interval lists.

#A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

#The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        out=[]
        while firstList and secondList:
            first1, first2= firstList[0]
            second1, second2= secondList[0]
            if first2< second1:
                firstList.pop(0)
            elif second2<first1:
                secondList.pop(0)
            else:
                x1, x2, x3, x4= sorted([first1, first2, second1, second2])
                # print(x1,x2,x3,x4)
                out.append([x2, x3])
                if x4==first2:
                    secondList.pop(0)
                else:
                    firstList.pop(0)
        return out
        
        
        