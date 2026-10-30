class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n2s = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

        digit = [int(d) for d in digits]
        res = []
        string = []
        if len(digits) ==0:
            return []

        def backtrack(i):

            
            if i == len(digit):
                res.append("".join(string))
                return

            letters = n2s[digit[i]]
            
            for j in letters:
                string.append(j)
                backtrack(i+1)
                string.pop()
            
        backtrack(0)
        return res

            

            



        


        