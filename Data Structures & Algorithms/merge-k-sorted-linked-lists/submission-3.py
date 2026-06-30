# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

            fakehead = ListNode(0)
            tail = fakehead

            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2= list2.next

                tail = tail.next

            if list1:
                tail.next = list1
            else:
                tail.next = list2
                
            return fakehead.next

        # merged = None
        # for lst in lists:
        #     merged = mergeTwoLists(merged, lst)

        # return merged
        # o(n*k)
        # o(nlogk)

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None

                mergedList.append(mergeTwoLists(list1,list2))


            lists = mergedList
        
        return mergedList[0]



            
    


            
        


        