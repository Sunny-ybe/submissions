# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        curr = dummy

        i = 0
        while i < n:
            fast= fast.next
            i+=1
        
        while fast.next:
            fast = fast.next
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next





        