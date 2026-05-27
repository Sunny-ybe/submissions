class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict= {}

        for e in strs:
            h = "".join(ch for ch in sorted(e))
            #key = h
            if h not in myDict:
                #key=f"{h}"
                myDict[h] = []
            myDict[h].append(e)
        return list(myDict.values())

        # better solution - best infact
        # res = defaultdict(list) no need to deal with edge xase of not having key
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')] +=1
        #     res[tuple(count)].append(s)
        # return res.values()
