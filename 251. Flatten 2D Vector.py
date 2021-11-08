# 251. Flatten 2D Vector
# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
#
# Implement the Vector2D class:
#
# Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
# hasNext() returns true if there are still some elements in the vector, and false otherwise.

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.fir, self.sec = 0, 0
        self.vec = vec
        while self.fir < len(self.vec) and self.sec == len(self.vec[self.fir]):
            self.fir += 1
            self.sec = 0

    def next(self) -> int:
        if not self.hasNext(): return None

        res = self.vec[self.fir][self.sec]
        self.sec += 1
        return res

    def hasNext(self) -> bool:
        while self.fir < len(self.vec) and self.sec == len(self.vec[self.fir]):
            self.fir += 1
            self.sec = 0
        return self.fir < len(self.vec) and self.sec < len(self.vec[self.fir])

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()