class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()



                if t=="+":
                    add = b+a
                    stack.append(add)
                    
                elif t=="-":
                    sub = a-b
                    stack.append(sub)
                    
                elif t=="*":
                    prod = a*b
                    stack.append(prod)

                else:
                    div = int(a/b)
                    stack.append(div)

        return int(stack[-1])


            

        
        