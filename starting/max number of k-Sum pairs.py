class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        dic = {}
        
        for x in nums:
            value = k - x
            if value in dic and dic[value] > 0:
                result += 1
                dic[value] -= 1
                
            else:
                if x not in dic:
                    dic[x] = 0
                dic[x]+=1 
                
        return result