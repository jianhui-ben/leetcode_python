# 2013. Detect Squares
# You are given a stream of points on the X-Y plane. Design an algorithm that:
#
# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.
#
# Implement the DetectSquares class:
#
# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

class DetectSquares:

    def __init__(self):
        self.stored = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.stored[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        out = 0
        for exist_point, fre in self.stored.items():
            ex_x, ex_y = exist_point
            if ex_x != x and ex_y != y and abs(ex_x - x) == abs(ex_y - y):
                out += self.stored[(ex_x, y)] * self.stored[(x, ex_y)] * fre

        return out
