class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
            
        while k > 0:
            k -= 1
            stack.pop()
                
        output = "".join(stack)
        return str(int(output)) if output else "0"