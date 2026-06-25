# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # curr = head
        # seen = set()
        # while curr:
        #     if curr not in seen:
        #         seen.add(curr)
        #         curr = curr.next
        #     else:
        #         return True

        # return False
        #fast and slow pointer
        fast = head
        slow = head
      
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
           
            
        return False




