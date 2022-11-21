class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        
        while left <= right and (score or power >= tokens[left]):
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif left != right:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
        return score