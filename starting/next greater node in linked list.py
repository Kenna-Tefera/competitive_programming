# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = -1
        output, stack = [], []
        
        while head:
            cur += 1
            output.append(0)
            
            while stack and stack[-1][1] < head.val:
                index, val = stack.pop()
                output[index] = head.val
            
            stack.append((cur, head.val))
            head = head.next
            
        return output