class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQue = deque()
        maxQue = deque()
        maxLen = 0
        st = 0
        
        for i in range(len(nums)):
            while minQue and minQue[-1] > nums[i]:
                minQue.pop()
            minQue.append(nums[i])
            
            while maxQue and maxQue[-1] < nums[i]:
                maxQue.pop()
            maxQue.append(nums[i])
        
            if maxQue[0] - minQue[0] <= limit:
                maxLen = max(maxLen, i - st + 1 )
            else:
                if maxQue[0] == nums[st]:
                    maxQue.popleft()
                if minQue[0] == nums[st]:
                    minQue.popleft()
                st += 1
        return maxLen