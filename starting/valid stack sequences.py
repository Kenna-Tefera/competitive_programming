class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ptr = 0
        
        for i in pushed:
            stack.append(i)
            while stack and ptr < len(popped) and stack[-1] == popped[ptr]:
                ptr += 1
                stack.pop()
        return stack == []