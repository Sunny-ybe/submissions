# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # very dumb way  -_-
        # lst1 = []
        # lst2 = []
        # curr1 = l1
        # curr2 = l2
        # i = 0
        # j=0

        # while curr1:
        #     lst1.append(curr1.val)
        #     curr1 = curr1.next
        #     i+=1
        
        # while curr2:
        #     lst2.append(curr2.val)
        #     curr2 = curr2.next
        #     j+=1
        
        # lst1 = lst1[::-1]
        # lst2= lst2[::-1]

        # res1 = "".join([str(item) for item in lst1])
        # res2 = "".join([str(item) for item in lst2])
        # # res2 = " ".join(lst2)

        # res = int(res1)+int(res2)
        
        # dummy = ListNode(0)
        # ans = dummy

        # digits = [int(digit) for digit in str(res)]

        # for d in reversed(digits):
        #     ans.next = ListNode(d)
        #     ans = ans.next

        # return dummy.next.  

        # smarter way

        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next




        



       
        



        
        