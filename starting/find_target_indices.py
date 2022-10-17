class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index = []
        for i in range (len(nums)):
            if nums[i] == target:
                index.append(i)
        return index
