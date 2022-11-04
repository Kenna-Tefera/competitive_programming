class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        num = ""
        nums = [str(x) for x in range(10)]
        
        for char in s:
            if char in nums:
                num += char
            elif char == "[":
                stack.append(["",int(num)])
                num =""
            elif char == "]":
                string_, k = stack.pop()
                stack[-1][0] += string_ * k
            else:
                stack[-1][0]  += char
                
        return stack[-1][0]