class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftpointer,  rightpointer = 0, 0
        total, result = 0, 0
        
        while rightpointer < len(nums):
            total += nums[rightpointer]
            
            while nums[rightpointer] * (rightpointer - leftpointer + 1) > total + k:
                total -= nums[leftpointer]
                leftpointer += 1
                
            result = max(result, rightpointer - leftpointer + 1)
            rightpointer += 1
            
        return result