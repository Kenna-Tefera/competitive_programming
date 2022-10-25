class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                
            elif s[i] == ")":
                indx = s[stack[-1]: i + 1]
                s = s[:stack[-1]] + indx[::-1] + s[i + 1:]
                stack.pop(-1)
        
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                ans += (s[i])
        return ans