# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None
        
        while curr != None:
            # store the curr.next in a node
            nextNode = curr.next

            # point the current node to the prev node
            curr.next = prev

            #move prev to curr for the next iteration    
            prev = curr
            #move curr to the nextNode.
            curr = nextNode
        return prev
