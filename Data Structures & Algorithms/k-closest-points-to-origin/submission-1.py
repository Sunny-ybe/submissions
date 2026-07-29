class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for p in points:
            d = p[0]*p[0] + p[1]*p[1]
            lst.append((d,p))

        res = []

        heapq.heapify(lst)

        for i in range(k):
            dist, point = heapq.heappop(lst)
            res.append(point)
        return res