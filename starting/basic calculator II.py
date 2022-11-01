class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        cur = prev = res = 0
        operation = "+"
        
        while i < len(s):
            cur_char = s[i]
            
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i]) #parsing
                    i += 1
                i -= 1
                
                if operation == "+":
                    res+= cur
                    prev = cur
                    
                elif operation == "-":
                    res -= cur 
                    prev = -cur
                
                elif operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                    
                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)
                    
                cur = 0 
            elif cur_char != " ":
                operation = cur_char
            i += 1
            
        return res