# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow has midpoint where I want to reverse / split two halves
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN
        
        
        first, second = head, prev
        while second:
            nextF = first.next
            nextS = second.next

            first.next = second
            second.next = nextF

            first = nextF
            second = nextS




        
        