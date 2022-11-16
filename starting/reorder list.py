# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        q = deque()
        cur = head
        while True:
            cur = cur.next
            if not cur:
                break
            q.append(cur)
            
        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next
                
            if head and q:
                temp = q.popleft()
                head.next = temp
                head = head.next
        head.next = None