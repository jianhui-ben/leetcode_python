#346. Moving Average from Data Stream

#Given a stream of integers and a window size, calculate the 
#moving average of all integers in the sliding window.

#Example 1:

#MovingAverage m = new MovingAverage(3);
#m.next(1) = 1 // return 1.00000
#m.next(10) = (1 + 10) / 2 // return 5.50000
#m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
#m.next(5) = (10 + 3 + 5) / 3 // return 6.00000


class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size=size
        self.array=[]
        self.cur_sum=0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.array)== self.size:
            self.cur_sum-= self.array[0]
            self.array=self.array[1:]
            
        self.array.append(val)
        self.cur_sum+=val
        return self.cur_sum/len(self.array)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)