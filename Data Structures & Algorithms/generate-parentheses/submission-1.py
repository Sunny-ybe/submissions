class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #key idea
        #open < n append ( and 
        #openN > closedN append ) 
        #openN==closedN==n = base case add to output

        # res = []
        # stack = []

        # def backtrack(openN, closedN):
        #     if openN==closedN==n:
        #         res.append("".join(stack))
        #         return

        #     if openN<n:
        #         stack.append("(")
        #         backtrack(openN+1, closedN)
        #         stack.pop()

        #     if openN > closedN:
        #         stack.append(")")
        #         backtrack(openN,closedN+1)
        #         stack.pop()
        # backtrack(0,0)
        # return res

        res = []
        stack = []

        def build(openN, closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                build(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                build(openN,closedN+1)
                stack.pop()
            
        build(0,0)
        return res

            






















        