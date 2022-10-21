class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        list = []
        ans = []
        checker = True
        
        for i, j in zip(l,r):
            list = nums[i : j+1]
            list.sort()
            
            for k in range(len(list) - 1):
                if list[k+1] - list[k] == list[1] - list[0]:
                    checker = True
                else:
                    checker = False
                    break
            ans.append(checker)
        return ans