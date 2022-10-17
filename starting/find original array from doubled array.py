class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        result = []
        count = Counter(changed)
        
        for i in changed:
            if i == 0 and count[i] >= 2:
                count[i] -=2
                result.append(i)
            elif i > 0 and count[i] and count[i*2]:
                count[i] -= 1
                count[i*2] -= 1
                result.append(i)
        return result if len(result) == len(changed) // 2 else []