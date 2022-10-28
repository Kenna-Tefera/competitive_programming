class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            next = -1
            for j in range(nums2.index(i) + 1, len(nums2)):
                if nums2[j] > i:
                    next = nums2[j]
                    break
            ans.append(next)
        return ans