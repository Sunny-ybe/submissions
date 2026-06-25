# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        #find the middle and end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #second = later half - split here
        second = slow.next
        slow.next = None

        # reverse the later half
        curr = second
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #prev = reversed other half 
        #now merge both from first to fast and prev into one

        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        # Reorder list = split, reverse second half, stitch.








            
        


        

        
        