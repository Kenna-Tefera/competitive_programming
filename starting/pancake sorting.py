class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n):
            max_ = max(arr[:n - i])
            max_indx = arr.index(max_) + 1
            arr[:max_indx] = reversed(arr[:max_indx] )
            ans.append(max_indx)
            arr[:n - i] = reversed(arr[:n - i])
            ans.append(n - i)
        return ans