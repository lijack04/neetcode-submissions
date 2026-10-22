# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        dummy = ListNode(0, head)

        beforeN, afterN = dummy, dummy

        for i in range(n):
            afterN = afterN.next
        
        while afterN and afterN.next:
            beforeN = beforeN.next
            afterN = afterN.next
        
        beforeN.next = beforeN.next.next

        return dummy.next