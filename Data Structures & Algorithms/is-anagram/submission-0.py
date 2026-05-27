class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #lst = "".join(ch.lower() for ch in s)
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        for ch in t:
            freq[ch] = freq.get(ch,0) - 1
        for key in freq:
            if freq[key] != 0:
                return False
        return True
        