class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        
        for indx, c in enumerate(citations):
            if indx >= c:
                return indx
        return len(citations)