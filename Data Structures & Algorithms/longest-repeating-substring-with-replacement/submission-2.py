class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = {}
        # l = 0
        # maxres = 0
        # for r in range(len(s)):
        #     count[s[r]] = count.get(s[r],0) + 1 
        #     if (r-l+1) - max(count.values()) <= k:
        #         res = r-l + 1
        #         maxres = max(res, maxres)
        #     else:
        #         count[s[l]] -= 1
        #         l+=1

        # return maxres

        # Standard Neetcode while pattern soln
        count = {}
        l = 0
        res = 0
        maxres = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) +1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1
            res = r-l+1
            maxres = max(res,maxres)
        return maxres





        
        
        
        