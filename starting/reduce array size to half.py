class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = 0
        result = 0
        
        for i,j in sorted(count.items(), key = lambda x: -x[1]):
            n += j
            result += 1
            if n >= (len(arr)//2): break
        return result