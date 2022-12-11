class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right, output = 0, k, 0
        summ = sum (arr[0:k])
        average = threshold * k
        if summ >= average:
            output += 1
            
        while right < len(arr):
            summ -= arr[left]
            summ += arr[right]
            if summ >= average:
                output += 1
            left += 1
            right += 1
        return output