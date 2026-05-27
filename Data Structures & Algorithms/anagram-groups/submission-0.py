class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict= {}

        for e in strs:
            h = "".join(ch for ch in sorted(e))
            key = h
            value = e
            if h not in myDict:
                key=f"{h}"
                myDict[key] = []
            myDict[key].append(e)
        return list(myDict.values())
