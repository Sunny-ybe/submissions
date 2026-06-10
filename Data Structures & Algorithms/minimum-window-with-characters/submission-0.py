class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        window = {}
        countT = {}

        for c in t:
            countT[c] = countT.get(c,0) + 1

        have = 0
        need = len(countT)
        res = ""
        reslen = float("infinity")
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0) +1

            if ch in countT and window[ch] == countT[ch]:
                have +=1

            while have == need:
                #update result
                if (r-l +1) < reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                #pop off left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
            

        return res if reslen != float("infinity") else ""
                

        



       




        
        