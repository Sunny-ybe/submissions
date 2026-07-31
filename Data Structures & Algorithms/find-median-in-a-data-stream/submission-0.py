class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)
        self.lst.sort()

    def findMedian(self) -> float:
        length = len(self.lst)
        if not self.lst:
            return None

        if len(self.lst) == 1:
            return self.lst[0]


        if length % 2 == 0:
            return ((self.lst[length//2]) + (self.lst[length//2 - 1])) / 2
        else:
            return self.lst[length//2]

        
        