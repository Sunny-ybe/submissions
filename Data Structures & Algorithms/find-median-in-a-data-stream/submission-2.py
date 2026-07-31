class MedianFinder:

    def __init__(self):
        self.nums = []
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not self.left or num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) > len(self.right) + 1:
            l = -heapq.heappop(self.left)
            heapq.heappush(self.right,l)

        if len(self.right) > len(self.left) + 1:
            r = heapq.heappop(self.right)
            heapq.heappush(self.left,-r)
        

    def findMedian(self) -> float:
        median = 0
        length = len(self.left) + len(self.right)
        if length == 0:
            return None
       
        if length % 2 == 0:
            return (-self.left[0] + self.right[0])/2

        else:
            if len(self.left) > len(self.right):
                median = -self.left[0]
            else:
                median = self.right[0]
        return median
        