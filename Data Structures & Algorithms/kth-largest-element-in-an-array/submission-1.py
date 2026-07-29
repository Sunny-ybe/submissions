class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap = nums
        # heapq.heapify(minheap)
        # while len(minheap)>k:
        #     heapq.heappop(minheap)
        # return heapq.heappop(minheap)

        minheap = [] #empty list is already a valid heap

        for n in nums:
            heapq.heappush(minheap, n)

            if len(minheap) > k:
                heapq.heappop(minheap)
            
        return minheap[0]


        
        