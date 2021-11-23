# 1146. Snapshot Array
# Implement a SnapshotArray that supports the following interface:
#
# SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

class SnapshotArray:
    """
    binary search
    """

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.cur_snap = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index] and self.arr[index][-1][0] == self.cur_snap:
            self.arr[index].pop()
        self.arr[index].append((self.cur_snap, val))

    def snap(self) -> int:
        self.cur_snap += 1
        return self.cur_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        find the last entry of (snap_id, val) where snap_id <= snap_id
        """
        # print(self.arr)
        left, right = 0, len(self.arr[index]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.arr[index][mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return self.arr[index][right][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)