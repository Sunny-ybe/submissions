class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for p in s:
            if p in "({[":
                stack.append(p)
            
            if p in ")}]":
                if not stack:
                    return False
                
                if len(stack) != 0:
                    
                    top = stack.pop()
                    if (p == ")" and top != "(") or (p == "}" and top != "{") or (p == "]" and top != "["):
                        return False
                
        return len(stack) == 0
        