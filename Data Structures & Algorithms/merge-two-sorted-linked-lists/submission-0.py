# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        a = list1
        b = list2

        head = ListNode()
        dummy = None
        first = True

        while a is not None or b is not None:

            if a is not None and b is not None:
                #compare a and b
                if a.val < b.val:
                    head.next = a
                    a = a.next
                elif a.val > b.val:
                    head.next = b
                    b = b.next
                else:
                    head.next = a
                    head = head.next

                    if first:
                        dummy = head
                        first = False

                    a = a.next
                    continue

            elif a is None:
                head.next = b
                b = b.next

            else: #b is None
                head.next = a
                a = a.next

            head = head.next

            if first:
                dummy = head
                first = False

        return dummy
            
            


        