class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        q = deque(piles)
        
        while len(q) > 0:
            q.popleft()
            q.pop()
            sum += q[-1]
            q.pop()
        return sum