class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k
        summ = sum(cardPoints[right:])
        res = summ
        
        while right < len(cardPoints):
            summ += (cardPoints[left] - cardPoints[right])
            res = max(res, summ)
            left += 1
            right += 1
            
        return res