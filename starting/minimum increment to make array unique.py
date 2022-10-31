class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        count = Counter(nums)
        maxx = max(nums)
        pre = -1
        
        for num in range(maxx + 1):
            cnt = count[num]
            
            if cnt > 0:
                totalMoves = 0
                maxMove = cnt -1
                totalMoves = maxMove * (maxMove + 1) //2
                maxNum = num + maxMove
                
                if num <= pre:
                    totalMoves += cnt * (pre - num + 1)
                    maxNum += pre - num + 1
                
                res += totalMoves
                pre = maxNum
        return res