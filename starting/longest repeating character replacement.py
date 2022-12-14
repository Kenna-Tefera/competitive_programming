class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, output = 0, 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]]-= 1
                left += 1
            output = max(output, right - left + 1)
        return output