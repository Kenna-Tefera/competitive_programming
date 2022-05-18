class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        stack=[]
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            if stack[-1][1]>=intervals[i][0]:
                stack[-1][0] = min(stack[-1][0], intervals[i][0])
                stack[-1][1] = max(stack[-1][1],intervals[i][1])
            else:
                stack.append(intervals[i])
        return stack
