class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            l1 = -heapq.heappop(maxHeap)
            l2 = -heapq.heappop(maxHeap)
            toadd = l1-l2
            heapq.heappush(maxHeap, -toadd)

        return abs(maxHeap[0])
        