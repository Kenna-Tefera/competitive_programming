class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(0, len(nums)-1):
            for j in range (i+1, len(nums)):    
                if nums[i] == nums[j] and i<j:
                    result = result + 1
        return result