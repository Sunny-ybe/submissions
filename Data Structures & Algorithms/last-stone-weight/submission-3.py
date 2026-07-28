class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            largest = -heapq.heappop(maxHeap)
            large2 = -heapq.heappop(maxHeap)

            toadd = (largest - large2)
            heapq.heappush(maxHeap, -toadd)
        
        return abs(maxHeap[0])

                


        