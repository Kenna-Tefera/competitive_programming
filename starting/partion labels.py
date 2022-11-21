class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for indx, char in enumerate(s):
            lastIndex[char] = indx
            
        result = []
        size , end = 0, 0
        for indx, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])
            
            if indx == end:
                result.append(size)
                size = 0
        return result