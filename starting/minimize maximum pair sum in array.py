class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minsum = 0
        
        for i in range(0, len(nums) // 2):
            minsum = max(minsum,nums[i] + nums[-1])
            nums.pop()
        return minsum