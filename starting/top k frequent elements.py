class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_nums = list(set(nums))
        freq = []
        result = []
        
        for i in new_nums:
            freq.append(nums.count(i))
        
        for j in range(k):
            index = freq.index(max(freq))
            result.append(new_nums[index])
            freq[index] =- 1
        return result