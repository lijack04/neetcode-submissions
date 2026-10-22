"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy = {None: None}

        old = head
        while old:
            oldtoCopy[old] = Node(old.val)
            old = old.next
        
        old = head
        while old:
            copy = oldtoCopy[old]
            copy.next = oldtoCopy[old.next]
            copy.random = oldtoCopy[old.random]
            old = old.next
        
        return oldtoCopy[head]

        

        