class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = "".join(char for char in num1)
        n2 = "".join(char for char in num2)


        return str(int(n1)*int(n2))

        

        