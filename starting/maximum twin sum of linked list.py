# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        res = 0
        
        while head:
            nums.append(head.val)
            head = head.next
        i = 0   
        while (i < (len(nums)/2)):
            twin = len(nums)-1-i
            res = max(res, (nums[i] + nums[twin]))
            i += 1
    
        return res