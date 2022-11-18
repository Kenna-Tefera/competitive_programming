class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        zeros = 0
        while start < len(nums):
            if nums[start] == 0:
                nums.pop(start)
                zeros += 1
                start -= 1
            start += 1
        
        while zeros:
            nums.append(0)
            zeros -= 1