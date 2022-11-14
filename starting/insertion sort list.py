# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head  
        
        while cur:
            prev = dummy
            nxt = dummy.next
            
            while nxt:
                if cur.val < nxt.val:
                    break
                prev = prev.next
                nxt = nxt.next
                
            temp = cur.next
            cur.next = nxt
            prev.next = cur
            
            cur = temp
            
        return dummy.next