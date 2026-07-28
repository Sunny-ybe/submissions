class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dis = {}
        lst = []
        for p in points:
            d = p[0]*p[0] + p[1]*p[1]
            # dis[p] = d
            lst.append((d,p))

        heapq.heapify(lst)
        res = []

        for i in range(k):
            dist, point = heapq.heappop(lst)
            res.append(point)
        
        return res
            

               


                



        