class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start, end = 0, len(people) - 1
        
        people.sort()
        boats = 0
        
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            boats += 1
            end -= 1
        return boats