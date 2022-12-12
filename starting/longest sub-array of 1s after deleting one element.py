class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, output = 0, 0, 0
        zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1 and left < len(nums):
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            right += 1
            output = max(output, right - left - 1)
        return output