class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_length, unique = 0, 0, 0
        count = Counter()
        
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            
            if count[fruits[right]] == 1:
                unique += 1
                
            while unique > 2:
                count[fruits[left]] -= 1
                
                if count[fruits[left]] == 0:
                    unique -= 1
                    
                left += 1
                
            cur_length = right - left + 1
            max_length = max(max_length, cur_length)
        return max_length