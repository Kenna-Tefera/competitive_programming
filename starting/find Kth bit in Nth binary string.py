class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(r):
            arr = []
            for i in r:
                if i == "0":
                    arr.append("1")
                else:
                    arr.append("0")
            return "".join(reversed(arr))
        
        r = "0"
        for _ in range(n):
            r = r + "1" + rec(r)
        return r[k - 1]