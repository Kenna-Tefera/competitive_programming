# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        else:
            cur = head
            while cur != None:
                if cur.next == None:
                    break
                temp = cur.val
                cur.val = cur.next.val
                cur.next.val = temp
                
                cur = cur.next.next
            return head