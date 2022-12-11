class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        left, right, vcount = 0, k - 1, 0
        
        for i in range(k):
            if s[i] in vowels:
                vcount += 1
        
        max_vcount = vcount
        while right < len(s)-1:
            if s[left] in vowels:
                vcount -= 1 
            left += 1
            right += 1
            if s[right] in vowels:
                vcount += 1
            max_vcount = max(max_vcount, vcount)
        return max_vcount