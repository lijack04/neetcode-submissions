# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(minHeap, (l.val, i, l))
        
        curr = ListNode(0, None)
        dummy = curr
        
        while minHeap:
            val, i, nextN = heapq.heappop(minHeap)
            curr.next = nextN
            curr = curr.next
            nextN = nextN.next
            if nextN:
                heapq.heappush(minHeap, (nextN.val, i, nextN))
        
        return dummy.next
        
    