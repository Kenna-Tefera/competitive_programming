class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]
        
        leftpointer = 0
        rightpointer = len(nums)-1
        
        while len(nums) != len(result):
            result.append(nums[leftpointer])
            leftpointer += 1
            
            if leftpointer <= rightpointer:
                result.append(nums[rightpointer])
                rightpointer -=1
            
        return result