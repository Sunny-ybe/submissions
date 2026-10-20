class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #lst = "".join(ch.lower() for ch in s)
        if len(s) != len(t):
            return False
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1
            if freq[c] < 0:
                return False
        # for key in freq:
        #     if freq[key] != 0:
        #         return False
        #above loop becomes optional now, all invariant is
        #already implemented
        return True
        #Cheat Algo using Python DS Counter
        # return sorted(s) == sorted(t)
        #return Counter(s) == Counter(t)
        