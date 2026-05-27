class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        lst = sorted(list(freq.values()))[::-1]
        for i in range(k):
            for num in freq:
                if freq[num] == lst[i] and num not in res:
                    res.append(num)
                    break
        return res
            
            
    
    

        
        