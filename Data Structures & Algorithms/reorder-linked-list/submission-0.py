# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        nodeAtIndex = []

        while head is not None:
            nodeAtIndex.append(head)
            head = head.next
        
        dummy = ListNode()
        start = dummy

        front = 0
        back = len(nodeAtIndex) - 1
        nodesLeft = len(nodeAtIndex)

        isFront = True

        while nodesLeft > 0:
            if(isFront):
                dummy.next = nodeAtIndex[front]
                front += 1
            else:
                dummy.next = nodeAtIndex[back]
                back -= 1
            
            dummy = dummy.next
            isFront = not isFront
            nodesLeft -= 1
        
        dummy.next = None
        head = start.next
        






