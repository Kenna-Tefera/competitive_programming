class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        x,i = 1,0
        
        while x <= n:
            if x == n: return True
            i += 1
            x = 3**i
        return False
        