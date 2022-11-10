class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        bottom_up = [None] * (n+1)
        bottom_up[0] = 0
        bottom_up[1] = 1
        for i in range(2, n+1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        return bottom_up[n]