class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")":"(", "}":"{", "]":"["}
        
        for par in s:
            if par in d.values():
                stack.append(par)
            elif stack and d[par] == stack [-1]:
                stack.pop()
            else:
                return False
        return stack == []