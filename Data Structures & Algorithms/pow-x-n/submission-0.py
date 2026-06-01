class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            for i in range(n):
                res = res * x
        elif n == 0:
            res = 1
        else:
            for i in range(abs(n)):
                res= (1/x) *res
        return res
        