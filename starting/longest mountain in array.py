class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        output = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                l = r = i
                while  l > 0 and arr[l] > arr[l-1]:
                    l -= 1
                
                while r < len(arr) - 1 and arr[r] > arr[r+1]:
                    r += 1
                output = max(output, (r - l + 1))
        return output